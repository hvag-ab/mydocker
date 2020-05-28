django项目目录结构：
xxx_project:

　　apps
　　　　app1
　　　　app2
　　　　app3
　　xxx_project
　　　　settings.py
　　　　urls.py
　　　　wsgi.py
　　templates
　　　　xxx.html
　　requirements.txt
　　manage.py
　　static
   media
　　conf
　　　　uwsgi.ini
　　nginx
　　　　Dockerfile
　　　　nginx.conf
　　　　uc_nginx.conf
　　Dockerfile
　　docker-compose.yml
　　docker-entrypoins.sh

web的Dockerfile
FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN echo python -V
RUN mkdir /docker_api
WORKDIR /docker_api
ADD . /docker_api
RUN pip install --upgrade pip
RUN  pip install -i https://pypi.douban.com/simple -r requirements.txt

nginx的Dockerfile

FROM nginx:latest
COPY uc_nginx.conf /etc/nginx/sites-available/
RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/uc_nginx.conf /etc/nginx/sites-enabled/
CMD ["nginx", "-g", "daemon off;"]

requirements.txt
pymysql
django
uwsgi
mysqlclient
djangorestframework
django-filter

docker-compose.yml配置文件
version: '3'
services:
    db:
      image: mysql:5.7
      expose:
        - 3306
      environment:
          MYSQL_DATABASE: xxxxxx
          MYSQL_ROOT_PASSWORD: xxxxxx
          MYSQL_USER: root
      volumes:
         - ./mycustom.cnf:/etc/mysql/conf.d/custom.cnf
         - ~/containers/mysql/data:/var/lib/mysql

    nginx:
      container_name: nginx-container
      restart: always
      depends_on:
        - web
      build: ./nginx
      ports:
        - 8080:80
      volumes:
        - .:/docker_api
    
    web:
       build: .
       restart: always
       command: uwsgi -i ./conf/uwsgi.ini
       volumes:
          - .:/docker_api
       ports:
          - 8000:8000
       depends_on:
          - db
       links:
          - db

uwsgi需要先启动起来，nginx才能去访问，启动uwsgi可以直接命令行带参数，或者可以写ini的配置文件去启动（这样会更新维护和管理）
这里涉及非常多的参数，目前还没完全搞懂
注意：一定要使用socket定义，并且跟nginx定义的端口一致，并且跟容器暴露的端口一致
注意：路径问题一定要处理好，这里是定义chdir跳去django项目的目录

[uwsgi]
chdir     = ./xxx_project
module    = conf.wsgi
socket    = :8000
processes = 4
threads   = 10
enable-threads
master-as-root

nginx需要修改配置去指向uwsgi，并且要指定static资源，这里只列出关键的位置

location /static {
    alias ./docker_api/xxx_project/static;
}
location / {
    include uwsgi_params;
    uwsgi_pass django:8000;
}
需要在settings.py文件中指定static目录，如果不指定会导致无法执行collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, “static/”)

执行collectstatic将所有静态文件都整理到指定目录
python manage.py collectstatic
