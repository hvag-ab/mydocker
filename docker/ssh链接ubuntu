二、开始安装
Windows的docker安装就不再多说了，网上有很多教程

在docker的hub仓库中，有专门的ubuntu系统。我们直接用使用就可以了。

1、打开cmd,拉取Ubuntu
docker pull ubuntu


2、查看拉取是否成功
docker images


3、运行容器
docker run --name iubuntu -t -i -d -p 3316:22 ubuntu
参数: –name 指定生成的容器的名称 
-i: 以交互模式运行容器，保证容器中STDIN是开启的。通常与 -t 同时使用； 
-t: 为容器重新分配一个伪tty终端，通常与 -i 同时使用； 
-d: 后台运行容器，并返回容器ID； 
-p:可以指定要映射的IP和端口，但是在一个指定端口上只可以绑定一个容器。支持的格式有 hostPort:containerPort、ip:hostPort:containerPort、 ip::containerPort。 
ubuntu 则是镜像名称，镜像ID也可以的。

 

4、查看是否运行成功
查看正在运行的镜像
docker ps


二、安装ssh服务
1、进入容器终端安装ssh服务
docker exec -t -i iubuntu /bin/bash


2、执行更新
apt-get update
 等待，输入Y就可以了



3、安装ssh-client、ssh-server
安装ssh-client命令
apt-get install openssh-client
等待，输入Y就可以了



安装ssh-server命令
apt-get install openssh-server
等待，输入Y就可以了



安装完成后，先启动服务
/etc/init.d/ssh start


查看是否正确启动

ps -e|grep ssh


编辑sshd_config文件
需要先安装vim编辑器
apt-get install vim


编辑sshd_config文件
vim /etc/ssh/sshd_config
添加 permitrootlogin yes  prl三个字母大写

保存退出  ESC + : + WQ

重启ssh服务
service ssh restart


设置ssh密码
passwd root
输入自己定义的密码 确认密码  比如1234


查看容器的IP
先安装net-tools工具包
apt-get install net-tools


查看IP
ifconfig
 

退出
exit


4、保存刚刚修改的镜像
docker commit  [容器ID/容器名]  [REPOSITORY:TAG]
三、使用Xshell连接
在本机连接可以用localhost:3316连接也可以用本机IP:3316连接  输入用户名 root 密码1234


然后连接就可以了 
 

