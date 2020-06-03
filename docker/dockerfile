## Dockerfile
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

