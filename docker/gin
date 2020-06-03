Dockerfile
在 go-gin-example 项目根目录创建 Dockerfile 文件，写入内容 确保所有的第三方库在这个下面

FROM golang:latest

RUN apt-get update && apt-get install -y vim
WORKDIR $GOPATH/src/go-gin-example
COPY . $GOPATH/src/go-gin-example
RUN go build -tags=jsoniter .

EXPOSE 8000
ENTRYPOINT ["./go-gin-example"]

作用
golang:latest 镜像为基础镜像，将工作目录设置为 $GOPATH/src/go-gin-example，并将当前上下文目录的内容复制到 $GOPATH/src/go-gin-example 中

在进行 go build 编译完毕后，将容器启动程序设置为 ./go-gin-example，也就是我们所编译的可执行文件

注意 go-gin-example 在 docker 容器里编译，并没有在宿主机现场编译

go-gin-example 的项目根目录下执行 docker build -t gin-blog-docker .


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
       volumes:
          - .:/docker_api
       ports:
          - 8000:8000
       depends_on:
          - db
       links:
          - db
