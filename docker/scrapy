创建dockfile
在 scrapy.cfg 文件所在的目录下面创建 dockfile ，里面的内容如下：

FROM python
MAINTAINER 1603753920@qq.com
RUN apt-get update \
	&& apt-get -y dist-upgrade \
	&& apt-get install -y openssh-server  \
	&& apt-get install -y python-pip3  \
	&& apt-get install -y zlib1g-dev libffi-dev libssl-dev  \
	&& apt-get install -y libxml2-dev libxslt1-dev  \
	&& apt-get install -y libmysqlclient-dev \ 
	&& apt-get install -y vim \ 
	&& pip install Scrapy \
	&& pip install pymysql \ 
	&& pip install redis \ 
	&& apt-get clean      \
 	&& apt-get autoclean  \
 	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY . /data
WORKDIR /data
CMD ["scrapy", "crawl", "spidername"]

编译镜像
在命令行进入dockerfile所在目录执行如下(改过程持续时间比较长)：

docker build -t spidername:1.0.0 .
编译完成之后可以通过如下的方式运行：

docker run --rm spidername:1.0.0

配置Crontab
在服务器上面创建一个 run.sh 的可执行文件，里面的内容如下：

#!/bin/bash

. /etc/profile
. ~/.bash_profile
docker run --rm spidername:1.0.0
使用 crontab -e 添加一条记录如下：

 * * * * sh /home/hvag/run.sh >> /home/hvag/log/log.`date +\%Y\%m\%d\%H\%M\%S` 2>&1
这样下来就实现了一个在Docker上面运行Scrapy采集任务的功能。




第二种
创建Dockerfile
首先在项目的根目录下新建一个requirements.txt文件，将整个项目依赖的Python环境包都列出来，如下所示：

requirements.txt 写入
scrapy>=1.7.0
pymysql
redis
在项目根目录下新建一个Dockerfile文件，文件不加任何后缀名，修改内容如下所示：

FROM python:3.6
ENV PATH /usr/local/bin:$PATH
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD scrapy crawl quotes

docker build -t quotes:latest .

docker run quotes


第三种

docker pull python:3.6
docker run -it python:3.6
进入python3.6容器里面

pip3 install scrapy 
mkdir /data 

exit

docker commit -m "ps" 容器id hvag/scrapypy 打包成镜像 一定要打包成镜像 否则下次进入python3.6镜像后 pip安装的库都会消失 

docker run -v $(pwd):/data -itd hvag/scrapypy  后台运行容器 注意pwd是当前主机所处的位置 一定要是你要运行的那个scrapy scrapy.cfg 所在的位置

docker exec -it d3a0aeaa9617 /bin/bash 进入容器
cd data   就可以在里面运行scrapy了 scrapy crawl xx







