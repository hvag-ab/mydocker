docker pull python:3.6
docker images
docker run -it python:3.6 /bin/bash bash启动python容器
python 进入python交互式环境

首先在当前目录下建立 mkdir -p myapp 然后在里面建立helloworld.py 
docker run  -v $PWD/myapp:/usr/src/myapp  -w /usr/src/myapp python:3.5 python helloworld.py
命令说明：

-v $PWD/myapp:/usr/src/myapp :将主机中当前目录下的myapp挂载到容器的/usr/src/myapp

-w /usr/src/myapp :指定容器的/usr/src/myapp目录为工作目录

python helloworld.py :使用容器的python命令来执行工作目录中的helloworld.py文件
