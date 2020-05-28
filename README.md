
Docker 是一个开源的应用容器引擎，而一个<ruby>容器<rt>containers</rt></ruby>其实是一个虚拟化的独立的环境，让开发者可以打包他们的应用以及依赖包到一个可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口。

- Docker 的局限性之一，它只能用在 64 位的操作系统上。

<!-- /TOC -->

Docker 从 `1.13` 版本之后采用时间线的方式作为版本号，分为社区版 `CE` 和企业版 `EE`，社区版是免费提供给个人开发者和小型团体使用的，企业版会提供额外的收费服务，比如经过官方测试认证过的基础设施、容器、插件等。

社区版按照 `stable` 和 `edge` 两种方式发布，每个季度更新 `stable` 版本，如 `17.06`，`17.09`；每个月份更新 `edge` 版本，如`17.09`，`17.10`。

下面教程运行在 `Centos` 中

## 新版本安装

Docker 官方的安装教程，[在这里](https://docs.docker.com/install/linux/docker-ce/centos/)。

安装一些必要的系统工具

```bash
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
```

添加软件源信息

```bash
# docker 官方源
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
# 阿里云源
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

可选：启用 `edge` 和 `test` 存储库。 这些存储库包含在上面的 `docker.repo` 文件中，但默认情况下处于禁用状态。您可以将它们与稳定存储库一起启用。

```
$ sudo yum-config-manager --enable docker-ce-edge
$ sudo yum-config-manager --enable docker-ce-test
```

您可以通过使用 `--disable` 标志运行 `yum-config-manager` 命令来禁用边缘或测试存储库。 要重新启用它，请使用 `--enable` 标志。 以下命令禁用 `edge` 存储库:

```bash
$ sudo yum-config-manager --disable docker-ce-edge
$ sudo yum-config-manager --disable docker-ce-test
```

安装 Docker-ce

```bash
# 安装前可以先更新 yum 缓存：
sudo yum makecache fast
# 安装 Docker-ce
sudo yum install docker-ce
```

如果你想安装特定 `docker-ce` 版本，先列出 repo 中可用版本，然后选择安装

```bash
$ yum list docker-ce --showduplicates | sort -r
# docker-ce.x86_64            18.06.1.ce-3.el7                   docker-ce-stable
# docker-ce.x86_64            18.06.1.ce-3.el7                   @docker-ce-stable
# docker-ce.x86_64            18.06.0.ce-3.el7                   docker-ce-stable
# docker-ce.x86_64            18.03.1.ce-1.el7.centos            docker-ce-stable
# docker-ce.x86_64            18.03.0.ce-1.el7.centos            docker-ce-stable
# docker-ce.x86_64            17.12.1.ce-1.el7.centos            docker-ce-stable
# 选择版本安装
$ sudo yum install docker-ce-<VERSION STRING>

# 选择安装 docker-ce-18.06.1.ce
$ sudo yum install docker-ce-18.06.1.ce
```

启动 Docker 后台服务

```bash
$ sudo systemctl start docker
```

通过运行 `hello-world` 镜像，验证是否正确安装了 `docker`。

```bash
$ docker run hello-world
```

## ubuntu安装

```bash
sudo apt-get remove docker docker-engine docker-ce docker.io  由于apt官方库里的docker版本可能比较旧，所以先卸载可能存在的旧版本：
sudo apt-get update 更新apt包索引：
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common 安装以下包以使apt可以通过HTTPS使用存储库（repository）：
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  添加Docker官方的GPG密钥
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce
systemctl status docker 查看是否启动
sudo systemctl start docker 启动docker服务

# 可以获得自己的加速器 https://××××××.mirror.aliyuncs.com

# echo "DOCKER_OPTS=\"--registry-mirror=https://××××××.mirror.aliyuncs.com\"" | sudo tee -a /etc/default/docker

# sudo systemctl docker restart
# docker info 查看
#=====================


## 命令介绍

```bash
$ docker --help

管理命令:
  container   管理容器
  image       管理镜像
  network     管理网络
命令：
  attach      介入到一个正在运行的容器
  build       根据 Dockerfile 构建一个镜像
  commit      根据容器的更改创建一个新的镜像
  cp          在本地文件系统与容器中复制 文件/文件夹
  create      创建一个新容器
  exec        在容器中执行一条命令
  images      列出镜像
  kill        杀死一个或多个正在运行的容器    
  logs        取得容器的日志
  pause       暂停一个或多个容器的所有进程
  ps          列出所有容器
  pull        拉取一个镜像或仓库到 registry
  push        推送一个镜像或仓库到 registry
  rename      重命名一个容器
  restart     重新启动一个或多个容器
  rm          删除一个或多个容器
  rmi         删除一个或多个镜像
  run         在一个新的容器中执行一条命令
  search      在 Docker Hub 中搜索镜像
  start       启动一个或多个已经停止运行的容器
  stats       显示一个容器的实时资源占用
  stop        停止一个或多个正在运行的容器
  tag         为镜像创建一个新的标签
  top         显示一个容器内的所有进程
  unpause     恢复一个或多个容器内所有被暂停的进程
```

## 服务管理

```bash
service docker start       # 启动 docker 服务，守护进程
service docker restart     #重新启动docker服务 守护进程
service docker stop        # 停止 docker 服务
service docker status      # 查看 docker 服务状态
chkconfig docker on        # 设置为开机启动
```

## 镜像管理

镜像可以看做我们平时装系统的镜像，里面就是一个运行环境。

```bash
docker pull centos:latest  # 从docker.io中下载centos镜像到本地
docker images [-a][-q]              # 查看已下载的镜像  q只显示image id a=all
docker rm image_id         # 删除镜像，指定镜像id
docker inspect 镜像名/id  查看镜像详细信息 
# 删除所有镜像
# none 默认为 docker.io
docker rmi image/imageid/image:tag 
docker rmi image:tag image:tag image:tag删除多个image
docker rmi $(docker images ubuntu -q) 删除所有ubuntu的镜像
```
## 查找镜像
1 通过 docker hub  https://registry.hub.docker.com   name:hvag pwd a475886877
2 docker search 镜像 最多返回25个镜像  -s or --stars表示 限定至少多少个星级
## 下载镜像
docker pull [option] NAME [:TAG]
## 推送镜像到docker hub上
docker push [option] NAME [:TAG]



## 容器管理

容器就像一个类的实例

```bash
# 列出本机正在运行的容器
docker container ls
# 列出本机所有容器，包括终止运行的容器
docker container ls --all
docker start [containerID/Names] # 启动容器
docker stop [containerID/Names]  # 停止容器
docker rm [-f] [containerID/Names]    # 删除容器 -f强制删除
docker logs [containerID/Names]  # 查看日志
docker exec -it [containerID/Names] /bin/bash  # 进入容器

# 从正在运行的 Docker 容器里面，将文件拷贝到本机，注意后面有个【点】拷贝到当前目录
docker container cp [containID]:[/path/to/file] .

docker run centos echo "hello world"  # 在docker容器中运行hello world!
docker run centos yum install -y wget # 在docker容器中，安装wget软件

docker ps                           # 列出包括未运行的容器
docker ps -a                        # 查看所有容器(包括正在运行和已停止的)
docker logs my-nginx                # 查看 my-nginx 容器日志

docker run -i -t centos /bin/bash   # 启动一个容器
docker run -i -t centos /bin/sh   # 启动一个容器
# 连接进行进入命令行模式，exit命令退出。  
docker run -t -i nginx:latest /bin/bash
###docker run -i -t ubuntu /bin/bash 进入ubuntu操作
#查看容器  如果docker ps 不给后面任何其他命令 返回的是正在运行的容器 
#docker ps [-a][-l]  -a表示所有  -l表示最新

docker inspect [容器id/容器名] 查看容器详细信息

docker run --name=hvag - i - t ubuntu /bin/bash 重命名ubuntu容器名字hvag


docker inspect centos     # 检查运行中的镜像
docker commit 8bd centos  # 保存对容器的修改
docker commit -m "n changed" my-nginx my-nginx-image # 使用已经存在的容器创建一个镜像
docker inspect -f {{.State.Pid}} 44fc0f0582d9 # 获取id为 44fc0f0582d9 的PID进程编号
# 下载指定版本容器镜像
docker pull gitlab/gitlab-ce:11.2.3-ce.0
```
docker logs [-f][-t] [--tail] 容器名 跟踪运行的容器 tail返回尾部多少数量日志 -f一直更新日志 需要ctr+c停止 -t表示显示带上时间戳

### 进入容器

1. 创建一个守护状态的Docker容器 适合运行服务和软件 -d以后台的形式启动程序 docker run -d image 守护进程运行

```bash
docker run -itd my-nginx /bin/bash
```
docker attach  容器id 进入已经运行的容器  在输入exit 退出容器 并停止容器

docker top 容器/容器id 命令查看运行的容器进程
2. 使用`docker ps`查看到该容器信息

```bash
docker ps


3. 使用`docker exec`命令进入一个已经在运行的容器

```bash
docker exec -it 6bd0496da64f /bin/bash
```
## 文件拷贝

从主机复制到容器 `sudo docker cp host_path containerID:container_path` 
示例 docker cp /www/runoob 96f7f14e99ab:/www/  将主机/www/runoob目录拷贝到容器96f7f14e99ab的/www目录下
从容器复制到主机 `sudo docker cp containerID:container_path host_path`
docker cp命令类似于UNIX中的cp -a命令，递归复制目录下的所有子目录和文件
-表示通过标准输入/输出设备以流的方式读取或写入tar文件
本地文件系统中的路径可以是绝对路径，也可以是相对路径，相对于当前命令执行的路径
容器中的路径都是相对容器的/根路径
被操作的容器可以是在运行状态，也可以是停止状态
不能复制/proc, /sys, /dev, tmpfs和容器中mount的路径下的文件

## 数据卷管理
docker volume ls 查看所有的数据卷
docker inspect test_db  详细查看 test_db数据卷信息 注意 Moutpoint 这是宿主机上数据卷的具体存放位置
可以看到数据卷test_db实际上存储在了本机的/var/lib/docker/volumes/test_db/_data上了。
skip-grant-tables
解决方法一: 删除数据卷

第一步:删除容器docker-compose rm -v
第二步:删除数据卷docker volume rm test_db
第三步:重新启动容器docker-compose up


##数据卷   保存数据到宿主机上 可以在容器之间共享和重用 可以备份与还原 不会随着容器删除而删除 一直存在
docker run -it -v /宿主机绝对路径目录:/容器内目录 镜像名/id
docker run -it -v /宿主机绝对路径目录:/容器内目录:ro 镜像名/id  ro表示只读 意思数据卷数据只能读取 不能写入

docker run -it -v ~/datavolume:/data ubuntu /bin/bash   datavolume保存在本地中 -v 指定使用数据卷
docker run -it -v $(pwd):/data ubuntu /bin/bash 
touch /data/c1 在容器中 data目录下建立c1文件
echo "i'm hvag" > /data/c1 输入 信息到 c1文件中
exit 退出bash
宿主机 cd datavolume/  就可以看到c1 文件夹  
vim c1 就可以看到im hvag了

容器之间共享数据
docker run --volumns-from [container name] 使用已经存在数据卷的容器的数据卷 就是共享数据
docker run -it --name con2 --volumns-from con1 ubuntu /bin/bash

数据卷备份与还原
备份
docker run --volumns-from [container name] -v $(pwd):/backup ubuntu
docker run  --volumns-from con1 -v ~/backup:/backup --name con2 ubuntu tar cvf /backup/con2.tar /datavolumn

docker save -o mynginx.tar 镜像名字
还原
docker load -i mynginx.tar

####端口映射
docker run -d --name nginx_1 -P nginx:latest 
通过docker ps可以看到nginx_1容器的80端口被映射到本机的32768端口上。访问宿主主机的32768端口就可以访问容器内的应用程序提供的Web界面

-p(小写p)可以指定要映射的端口，并且在一个指定的端口上只可以绑定一个容器。支持的格式有：IP:HostPort:ContainerPort | IP::ContainerPort | HostPort:ContainerPort 。
docker run -itd -p 5000:5000 --name nginx_2 nginx:latest 
可以使用IP:HostPort:ContainerPort格式指定映射使用一个特定地址：
docker run -itd -p 10.0.0.31:89:8081 --name nginx_4 nginx:latest 
使用IP::ContainerPort格式绑定本机的任意端口到容器的指定端口：
docker run -itd -p 10.0.0.31::8082 --name nginx_5 nginx:latest 
docker port nginx_1

### 容器中部署nginx

```bash
docker run -p 80 --name web -i -t ubuntu /bin/bash 启动ubuntu容器 对外接口80 
apt-get update 这个命令的作用是：同步 /etc/apt/sources.list 和 /etc/apt/sources.list.d 中列出的源的索引，这样才能获取到最新的软件包。否则下面步骤都失败 
apt-get install -y nginx
apt-get install -y vim
mkdir -p /var/www/html
cd /var/www/html
vim index.html 写一个html脚本
whereis nginx
ls /etc/nginx/sites-enabled 
vim /etc/nginx/sites-enabled/default 修改root中的默认的html 为刚才建立的html
nginx 启动nginx
ps -ef 查看nginx是否启动
ctr+p  ctr+q 退出容器 且让容器在后台运行
docker ps 查看运行中的容器
docker port web 查看web容器端口映射情况
docker top web 查看web容器进程情况
然后在浏览器中输入 http://127.0.0.1:32768 查看nginx服务  这个端口32768 是docker port 里面查找看到的
docker inspect web 查找容器的ip地址 和映射的端口
可以用容器的ip地址访问 

docker stop web 停止容器
docker start -i  web 启动容器 通过ps -ef查看  nginx 并没有启动
ctr+p  ctr+q 退出容器 且让容器在后台运行
docker exec web nginx 然后启动nginx




docker run -itd --name my-nginx2 nginx # 通过nginx镜像，【创建】容器名为 my-nginx2 的容器
docker start my-nginx --restart=always    # 【启动策略】一个已经存在的容器启动添加策略
                               # no - 容器不重启
                               # on-failure - 容器推出状态非0时重启
                               # always - 始终重启
docker start my-nginx               # 【启动】一个已经存在的容器
docker restart my-nginx             # 【重启】容器
docker stop my-nginx                # 【停止运行】一个容器 需要等待容器运行完毕
docker kill my-nginx                # 【杀死】一个运行中的容器
docker rename my-nginx new-nginx    # 【重命名】容器
docker rm new-nginx                 # 【删除】容器
```

容器使用状况监控
$ docker stats
默认情况下，stats 命令会每隔 1 秒钟刷新一次输出的内容直到你按下 ctrl + c。下面是输出的主要内容：
[CONTAINER]：以短格式显示容器的 ID。
[CPU %]：CPU 的使用情况。
[MEM USAGE / LIMIT]：当前使用的内存和最大可以使用的内存。
[MEM %]：以百分比的形式显示内存使用情况。
[NET I/O]：网络 I/O 数据。
[BLOCK I/O]：磁盘 I/O 数据。
[PIDS]：PID 号。

 --no-stream 选项只输出当前的状态：
$ docker stats --no-stream
$ docker stats --no-stream registry 1493 查看指定的容器状态 1493表示容器id
$ docker stats $(docker ps --format={{.Names}})
$ docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"



### 通过容器创建镜像

我们可以通过以下两种方式对镜像进行更改。

1. 从已经创建的容器中更新镜像，并且提交这个镜像
2. 使用 Dockerfile 指令来创建一个新的镜像

下面通过已存在的容器创建一个新的镜像。
docker commit [options] container [repository[:tag]] -a or --author表示作者 -m表示提交信息
```bash
docker commit -m="First Docker" -a="hvag" a6b0a6cfdacf hvag/nginx:v1.2.1
```

上面命令参数说明：

- `-m` 提交的描述信息
- `-a` 指定镜像作者
- `a6b0a6cfdacf` 记住这个是容器id，不是镜像id
- `hvag/nginx:v1.2.1` 创建的目标镜像名

关于dockerfile
虽然我们可以通过docker commit命令来手动创建镜像，但是通过Dockerfile文件，可以帮助我们自动创建镜像，并且能够自定义创建过程。本质上，Dockerfile就是由一系列命令和参数构成的脚本，这些命令应用于基础镜像并最终创建一个新的镜像。它简化了从头到尾的构建流程并极大的简化了部署工作。使用dockerfile构建镜像有以下好处：


Dockerfile指令 指令全部大写 #表示注释
我们需要了解一些基本的Dockerfile 指令，Dockerfile 指令为 Docker 引擎提供了创建容器映像所需的步骤。这些指令按顺序逐一执行。以下是有关一些基本 Dockerfile 指令的详细信息。

1.FROM
FROM 指令用于设置在新映像创建过程期间将使用的容器映像。
示例：
FROM nginx
FROM microsoft/dotnet:2.1-aspnetcore-runtime

1.1 MAINTAINER 
示例：
MAINTAINER hvag 1603753920@qq.com 作者 作者邮箱

2.RUN
RUN 指令指定将要运行并捕获到新容器映像中的命令。 这些命令包括安装软件、创建文件和目录，以及创建环境配置等。

格式：

RUN ["", "", ""] （exec模式）

RUN <command> (shell模式)

示例：

RUN apt-get update

RUN mkdir -p /usr/src/redis

RUN apt-get update && apt-get install -y libgdiplus

RUN ["apt-get","install","-y","nginx"]

注意：每一个指令都会创建一层，并构成新的镜像。当运行多个指令时，会产生一些非常臃肿、非常多层的镜像，不仅仅增加了构建部署的时间，也很容易出错。因此，在很多情况下，我们可以合并指令并运行，例如：RUN apt-get update && apt-get install -y libgdiplus。在命令过多时，一定要注意格式，比如换行、缩进、注释等，会让维护、排障更为容易，这是一个比较好的习惯。使用换行符时，可能会遇到一些问题，具体可以参阅下节的转义字符。

 
3.COPY
COPY 指令将文件和目录复制到容器的文件系统。文件和目录需位于相对于 Dockerfile 的路径中。

格式：
COPY
如果源或目标包含空格，请将路径括在方括号和双引号中。

COPY ["", ""]
示例：

COPY . .

COPY nginx.conf /etc/nginx/nginx.conf

COPY . /usr/share/nginx/html

COPY hom* /mydir/

 
4.ADD
ADD 指令与 COPY 指令非常类似，但它包含更多功能。除了将文件从主机复制到容器映像，ADD 指令还可以使用 URL 规范从远程位置复制文件。还可以解压文件

格式：

ADD<source> <destination>

示例：

ADD https://www.python.org/ftp/python/3.5.1/python-3.5.1.exe /temp/python-3.5.1.exe

此示例会将 Python for Windows下载到容器映像的 c:\temp 目录。

66 VOLUME数据卷
示例
VOLUME ["/data","/myvolume"] 向容器根目录新建两个文件夹作为容器数据卷
运行生成的这个镜像容器  然后 docker inspect 容器id 查找绑定在宿主机上对应的文件夹  这是docker自动生成绑定的

5.WORKDIR
WORKDIR 指令用于为其他 Dockerfile 指令（如 RUN、CMD）设置一个工作目录，并且还设置用于运行容器映像实例的工作目录。
默认 工作目录就是根目录 /  就是登陆容器后 所处的位置 

示例：
WORKDIR /app

6.CMD
CMD指令用于设置部署容器映像的实例时要运行的默认命令。例如，如果该容器将承载 NGINX Web 服务器，则 CMD 可能包括用于启动Web服务器的指令，如 nginx.exe。 如果 Dockerfile 中指定了多个CMD 指令，只会计算最后一个指令。

示例：

CMD ["c:\\Apache24\\bin\\httpd.exe", "-w"]

CMD c:\\Apache24\\bin\\httpd.exe -w

 
7.ENTRYPOINT
配置容器启动后执行的命令，并且不可被 docker run 提供的参数覆盖。每个 Dockerfile 中只能有一个ENTRYPOINT，当指定多个时，只有最后一个起效。

格式：

ENTRYPOINT ["", ""]

示例：

ENTRYPOINT ["dotnet", "Magicodes.Admin.Web.Host.dll"]

8.ENV
ENV命令用于设置环境变量。这些变量以”key=value”的形式存在，并可以在容器内被脚本或者程序调用。这个机制给在容器中运行应用带来了极大的便利。

格式：

ENV==...

示例：

ENV VERSION=1.0 DEBUG=on \

NAME="Magicodes"

 

9.EXPOSE
EXPOSE用来指定端口，使容器内的应用可以通过端口和外界交互。

格式：

EXPOSE

示例：

EXPOSE 80

10 USER  以什么身份运行 默认是root用户
USER  user  or user:group

11 ONBUILD 为镜像添加触发器
 当子镜像继承了父镜像 父镜像onbuild被触发
示例
ONBUILD RUN echo "father onbuild --- 23" 

转义字符
在许多情况下，Dockerfile 指令需要跨多个行；这可通过转义字符完成。 默认 Dockerfile 转义字符是反斜杠 \。 由于反斜杠在 Windows 中也是一个文件路径分隔符，这可能导致出现问题。

以下示例显示使用默认转义字符跨多个行的单个 RUN 指令。

FROM microsoft/windowsservercore

 

RUN powershell.exe -Command \

$ErrorActionPreference = 'Stop'; \

wget https://www.python.org/ftp/python/3.5.1/python-3.5.1.exe -OutFile c:\python-3.5.1.exe ; \

Start-Process c:\python-3.5.1.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait ; \

Remove-Item c:\python-3.5.1.exe -Force

 

要修改转义字符，必须在 Dockerfile 最开始的行上放置一个转义分析程序指令。 如以下示例所示：

# escape=`

 

FROM microsoft/windowsservercore

 

RUN powershell.exe -Command `

$ErrorActionPreference = 'Stop'; `

wget https://www.python.org/ftp/python/3.5.1/python-3.5.1.exe -OutFile c:\python-3.5.1.exe ; `

Start-Process c:\python-3.5.1.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait ; `

Remove-Item c:\python-3.5.1.exe -Force

注意，只有两个值可用作转义字符：\ 和 ` 。



下面是一些优化的准则：

选择合适的基础镜像

这点相对最为重要。为什么这么说，我们结合现实社会也可以看到，在大部分情况下，一个人一生的成就更多的是看出身。很多情况下，基因和出身决定了你的高度和终点，这点拿到技术层面来说，也是有很大道理的，因此我们需要选择合适的父母——一个合适的镜像。

一个合适的基础镜像是指能满足运行应用所需要的最小的镜像，理论上是能用小的就不要用大的，能用轻量的就不要用重量级的，能用性能好的就不要用性能差的。这里有时候还需要考虑那些能够减少我们构建层数的基础镜像。

 

优化指令顺序

Docker会缓存Dockerfile中尚未更改的所有步骤，但是，如果更改任何指令，将重做其后的所有步骤。也就是指令3有变动，那么4、5、6就会重做。因此，我们需要将最不可能产生更改的指令放在前面，按照这个顺序来编写dockerfile指令。这样，在构建过程中，就可以节省很多时间。比如，我们可以把WORKDIR、ENV等命令放前面，COPY、ADD放后面。

 

合并指令

前面其实我们提到过这点，甚至还特地讲到了转义字符，其实主要是为此服务。前面我们说到了，每一个指令都会创建一层，并构成新的镜像。当运行多个指令时，会产生一些非常臃肿、非常多层的镜像，不仅仅增加了构建部署的时间，也很容易出错。因此，在很多情况下，我们可以合并指令并运行，例如：RUN apt-get update && apt-get install -y libgdiplus。在命令过多时，一定要注意格式，比如换行、缩进、注释等，会让维护、排障更为容易，这是一个比较好的习惯。

 

删除多余文件和清理没用的中间结果

这点很易于理解，通常来讲，体积更小，部署更快！因此在构建过程中，我们需要清理那些最终不需要的代码或文件。比如说，临时文件、源代码、缓存等等。

  

使用 .dockerignore

.dockerignore文件用于忽略那些镜像构建时非必须的文件，这些文件可以是开发文档、日志、其他无用的文件。例如:



### 通过Dockerfile创建镜像

假设创建一个 node.js 镜像，首先在 node.js 项目根目录创建文件。

```bash
touch Dockerfile .dockerignore
```

`.dockerignore` 文件内容，下面代码表示，这三个路径要排除，不要打包进入 image 文件。如果你没有路径要排除，这个文件可以不新建。

```bash
.git
node_modules
npm-debug.log
```

Dockerfile 文件内容

```Dockerfile
FROM node:8.4
COPY . /app
WORKDIR /app
RUN npm install --registry=https://registry.npm.taobao.org
EXPOSE 3000
```

- `FROM node:8.4`：该 `image` 文件继承官方的 `node image`，冒号表示标签，这里标签是`8.4`，即`8.4`版本的 `node`。
- `COPY . /app`：将当前目录下的所有文件（除了 `.dockerignore` 排除的路径），都拷贝进入 `image` 文件的 `/app` 目录。
- `WORKDIR /app`：指定接下来的工作路径为`/app`。
- `RUN npm install`：在/app目录下，运行 `npm install` 命令安装依赖。注意，安装后所有的依赖，都将打包进入 `image` 文件。
- `EXPOSE 3000`：将容器 `3000` 端口暴露出来， 允许外部连接这个端口。

有了 `Dockerfile` 文件以后，就可以使用 `docker image build` 命令创建 `image` 文件了。

```bash
$ docker image build -t koa-demo .   注意 . 不能忘记掉 否则构建失败
# 或者
$ docker image build -t koa-demo:0.0.1 .
```

上面命令，`-t` 参数用来指定 `image` 文件的名字，后面还可以用冒号指定标签。如果不指定，默认的标签就是 `latest`。注意后面有个 `.`，表示 Dockerfile 文件所在的路径为当前路径 `-f` 表示指定dockerfile所在的路径 -f /mydocker/dockerfile 如果在当前dockerfile文件夹中 就可以省略不写

默认情况是docker构建的时候用缓存
docker build --no-cache 不使用缓存

### 发布自己的镜像

1. 在[Docker](https://www.docker.com/) 注册账户，发布的镜像都在[这个页面里](https://cloud.docker.com/repository/list)展示
2. 将上面做的镜像`nginx`，起个新的名字`nginx-test`

```bash
docker tag wcjiang/nginx:v1.2.1 wcjiang/nginx-test:lastest
```

3. 登录docker

```
docker login
```

4. 上传`nginx-test`镜像

```bash
docker push hvag/nginx-test:lastest
# The push refers to a repository [docker.io/hvag/nginx-test]
# 2f5c6a3c22e3: Mounted from hvag/nginx
# cf516324493c: Mounted from hvag/nginx
# lastest: digest: sha256:73ae804b2c60327d1269aa387cf782f664bc91da3180d10dbd49027d7adaa789 size: 736
```

### 镜像中安装软件

通常情况下，使用docker官方镜像，如 mysql镜像，默认情况下镜像中啥软件也没有，通过下面命令安装你所需要的软件：

```bash
# 第一次需要运行这个命令，确保源的索引是最新的
# 同步 /etc/apt/sources.list 和 /etc/apt/sources.list.d 中列出的源的索引
apt-get update
# 做过上面更新同步之后，可以运行下面的命令了
apt-get install vim
```

如果你安装了CentOS或者Ubuntu系统可以进入系统安装相关软件

```bash
# 进入到centos7镜像系统
docker run -i -t centos:7 /bin/bash
yum update
yum install vim
```




## Docker私有仓库搭建

通过官方提供的私有仓库镜像`registry`来搭建私有仓库。通过 [humpback](https://humpback.github.io) 快速搭建轻量级的Docker容器云管理平台。关于仓库配置说明请参见[configuration.md](https://github.com/docker/distribution/blob/master/docs/configuration.md)

> ⚠️ 注意：也可以通过部署管理工具 `Harbor` 来部署 `registry`

除了 [Harbor](https://github.com/goharbor/harbor) 还有 [humpback](https://github.com/humpback/humpback) 和 [rancher](https://github.com/rancher/rancher)

### `registry`

```bash
docker pull registry:2.6.2
```

创建容器并运行，创建成功之后，可访问 `http://192.168.99.100:7000/v2/`，来检查仓库是否正常运行，当返回 `{}` 时，表示部署成功。

```bash
docker run -d \
  -p 5000:5000 \
  --restart=always \
  --name registry \
  registry:2

# 自定义存储位置
docker run -d \
  -p 5000:5000 \
  --restart=always \
  --name registry \
  -v $HOME/_docker/registry:/var/lib/registry \
  registry:2

docker run -d -p 5000:5000 --restart=always --name registry \
    -v `pwd`/config.yml:/etc/docker/registry/config.yml \
    registry:2
```

推送镜像到私有仓库

```bash
# 从官方仓库拉取一个镜像
docker pull nginx:1.13
# 为镜像 `nginx:1.13` 创建一个新标签 `192.168.31.69:7000/test-nginx:1.13`
docker tag nginx:latest 192.168.31.69:5000/test-nginx:1.13
# 推送到私有仓库中
docker push 192.168.31.69:5000/test-nginx:1.13
# The push refers to a repository [192.168.99.100:7000/test-nginx]
# Get https://192.168.99.100:7000/v1/_ping: http: server gave HTTP response to HTTPS client
```

在推送到的时候报错误，默认是使用`https`提交，这个搭建的默认使用的是 `http`，解决方法两个：

1. 创建一个https映射
2. 将仓库地址加入到不安全的仓库列表中

我们使用第二种方法，加入到不安全的仓库列表中，修改docker配置文件`vi /etc/docker/daemon.json` 添加 `insecure-registries`配置信息，如果 [daemon.json](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file) 文件不存在可以创建，关键配置项，将仓库将入到不安全的仓库列表中。

```js
{
  "insecure-registries":[ 
    "192.168.31.69:5000"
  ]
}
```

>  如果是 macOS 可以通过 docker 客户端，`Preferences` => `Advanced` => `添加配置` => `Apply & Restart`，重启docker就可以了。  

重启服务 `service docker restart`，默认情况下 push 是会报如下错误的：

```bash
docker push 192.168.99.100:7000/test-nginx:1.13
# The push refers to a repository [192.168.99.100:7000/test-nginx]
# a1a53f8d99b5: Retrying in 1 second
# ...
# received unexpected HTTP status: 500 Internal Server Error
```

上面错误是 `SELinux` 强制访问控制安全系统，阻止导致的错误，通过下面方法禁用 SELinux 之后就可以 push 了。

```bash
setenforce 0  
getenforce   
# Permissive  
```

```bash
# 停止本地 registry
docker container stop registry
# 要删除容器，请使用 docker container rm
docker container stop registry && docker container rm -v registry
# 自定义存储位置
```

### `Harbor`

[部署 registry 管理工具 Harbor](docker/harbor.md)

## 使用Docker实战

> ⚠文件挂载注意：docker 禁止用主机上不存在的文件挂载到 container 中已经存在的文件

```bash
-d, --detach=false      # 指定容器运行于前台还是后台，默认为false   
-i, --interactive=false # 打开STDIN，用于控制台交互  
-t, --tty=false         # 分配tty设备，该可以支持终端登录，默认为false  
-u, --user=""           # 指定容器的用户  
-a, --attach=[]         # 登录容器（必须是以docker run -d启动的容器）
-w, --workdir=""        # 指定容器的工作目录 
-c, --cpu-shares=0      # 设置容器CPU权重，在CPU共享场景使用  
-e, --env=[]            # 指定环境变量，容器中可以使用该环境变量  
-m, --memory=""         # 指定容器的内存上限  
-P, --publish-all=false # 指定容器暴露的端口  
-p, --publish=[]        # 指定容器暴露的端口 
-h, --hostname=""       # 指定容器的主机名  
-v, --volume=[]         # 给容器挂载存储卷，挂载到容器的某个目录  
--volumes-from=[]       # 给容器挂载其他容器上的卷，挂载到容器的某个目录
--cap-add=[]            # 添加权限，权限清单详见：http://linux.die.net/man/7/capabilities  
--cap-drop=[]           # 删除权限，权限清单详见：http://linux.die.net/man/7/capabilities  
--cidfile=""            # 运行容器后，在指定文件中写入容器PID值，一种典型的监控系统用法  
--cpuset=""             # 设置容器可以使用哪些CPU，此参数可以用来容器独占CPU  
--device=[]             # 添加主机设备给容器，相当于设备直通  
--dns=[]                # 指定容器的dns服务器  
--dns-search=[]         # 指定容器的dns搜索域名，写入到容器的/etc/resolv.conf文件  
--entrypoint=""         # 覆盖image的入口点  
--env-file=[]           # 指定环境变量文件，文件格式为每行一个环境变量  
--expose=[]             # 指定容器暴露的端口，即修改镜像的暴露端口  
--link=[]               # 指定容器间的关联，使用其他容器的IP、env等信息  
--lxc-conf=[]           # 指定容器的配置文件，只有在指定--exec-driver=lxc时使用  
--name=""               # 指定容器名字，后续可以通过名字进行容器管理，links特性需要使用名字  
--net="bridge"          # 容器网络设置:
                            # bridge 使用docker daemon指定的网桥     
                            # host 	//容器使用主机的网络  
                            # container:NAME_or_ID  >//使用其他容器的网路，共享IP和PORT等网络资源  
                            # none 容器使用自己的网络（类似--net=bridge），但是不进行配置 
--privileged=false      # 指定容器是否为特权容器，特权容器拥有所有的capabilities  
--restart="no"          # 指定容器停止后的重启策略:
                            # no：容器退出时不重启  
                            # on-failure：容器故障退出（返回值非零）时重启 
                            # always：容器退出时总是重启  
--rm=false              # 指定容器停止后自动删除容器(不支持以docker run -d启动的容器)  
--sig-proxy=true        # 设置由代理接受并处理信号，但是SIGCHLD、SIGSTOP和SIGKILL不能被代理
```


首先创建放持久化数据文件夹，`mkdir -p /opt/app/humpback-web`，里面存放持久化数据文件，会存储站点管理和分组信息，启动后请妥善保存。

```bash
# 创建放持久化数据文件夹
mkdir -p /opt/app/humpback-web
# 下载humpback-web镜像到本地
docker pull humpbacks/humpback-web:1.0.0
# 启动 humpback-web 容器，将容器命名为 humpback-web
docker run -d --net=host --restart=always \
 -e HUMPBACK_LISTEN_PORT=7001 \
 -v /opt/app/humpback-web/dbFiles:/humpback-web/dbFiles \
 --name humpback-web \
 humpbacks/humpback-web:1.0.0
```

访问站点，打开浏览器输入：http://192.168.99.100:7001 ，默认账户：`admin` 密码：`123456`


## network 代替 link  在启动db容器的时候并没有使用-p或者-P参数，从而避免了暴露数据库服务端口到外部网络上。
Usage:  docker network COMMAND

Manage networks

Commands:
  connect     将一个容器连接到某一个网络
  create      创建一个网络
  disconnect  从某个网络中断开某一个容器的连接
  inspect     查看所有网络的详细信息
  ls          List networks
  prune       Remove all unused networks
  rm          Remove one or more networks


1.创建网络
docker network create wp-net

docker network ls 查看虚拟网卡的信息

docker run -d -p 3316:3306 --name wp-mysql --network wp-net --network-alias mysql -e MYSQL_ROOT_PASSWORD=123 mysql

说明：

docker run：启动容器

-d：后台运行

-p 3316:3306：将容器的3306端口映射到宿主机的3306端口上

--name wp-mysql：指定容器的名称为wp-mysql

--network wp-net：将容器加入到wp-net网络中

--network-alias mysql：指定容器在wp-net网络中的别名是mysql

-e MYSQL_ROOT_PASSWORD=123：初始化数据库root用户的密码为123


docker run --name py1 --network wp-net -d python
说明：
docker exec -it py1 /bin/bash


验证在py1容器中是否能与数据库通信
C:\Users\zsl-pc>docker exec -it wp-web /bin/bash
apt-get update
apt-get install -y iputils-ping
root@202fdad27426:ping -w 2 mysql
PING mysql (172.19.0.2): 56 data bytes
64 bytes from 172.19.0.2: icmp_seq=0 ttl=64 time=0.049 ms
64 bytes from 172.19.0.2: icmp_seq=1 ttl=64 time=0.155 ms
--- mysql ping statistics ---
3 packets transmitted, 2 packets received, 33% packet loss
round-trip min/avg/max/stddev = 0.049/0.102/0.155/0.053 msp
或者 进入python 环境  
import pymysQL r = pymysQl.connect host = wp-mysql 端口号用别名
说明：说明能够在wp-web容器中使用mysql数据库。


//查看 wp-net 网络里面的容器
docker inspect wp-net

//手动将某个容器加入网桥
docker network connect my-bridage test2

容器之间的访问可以使用【服务名:端口】的形式，或者【别名:端口】的形式。