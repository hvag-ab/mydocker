
## 下载镜像

拉取官方的镜像，标签为`5.7`，[Docker官方资料](https://docs.docker.com/samples/library/mysql/#-via-docker-stack-deploy-or-docker-compose)、[MySQL 官方资料](https://dev.mysql.com/doc/refman/8.0/en/docker-mysql-more-topics.html)，[MySQL镜像](https://hub.docker.com/_/mysql/)

```bash
docker pull mysql:5.7.23
# Trying to pull repository docker.io/library/mysql ...
# 5.7: Pulling from docker.io/library/mysql
# 85b1f47fba49: Already exists
# f34057997f40: Pull complete
# ....
# Digest: sha256:bfb22e93ee87c6aab6c1c9a4e70f28fa289f9ffae9fe8e173
```

## 运行容器示

```bash
sudo docker run --name mysql \
  -p 3316:3306 \
  -v $HOME/_docker/mysql/conf.d:/etc/mysql/conf.d \
  -v $HOME/_docker/mysql/data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -d mysql #-d表示后台运行mysql
```
#如果运行发现 报错重复名字的 也就是以前存在一个 那么docker ps -a 查看那个重复的 rm删除就可以了 如果3306被占用 那么把宿主机3306端口停止运行服务 

- `--name mysql`：容器名字为 `mysql`
- `-p 3316:3306`：将容器的 3306 端口映射到主机的 3316 端口
- `-v $HOME/_docker/mysql/conf.d`：将主机当前目录下的 `~/_docker/mysql/conf.d` 挂载到容器的 `/etc/mysql/conf.d`，这个是挂载配置目录
- `-v $HOME/_docker/mysql/data`：将主机当前目录下的 data 目录挂载到容器的 `/var/lib/mysqs`，为数据文件存放路径
- `-e MYSQL_ROOT_PASSWORD=123456`：初始化root用户的密码

docker ps 查看是否后台运行 如果没有查看到
docker logs mysql 查看运行日志
如果出现 chown: changing ownership of '/var/lib/mysql/conf.d': Operation not permitted
那么粗暴的方法就是删除 $HOME/_docker/mysql/data 这个目录下的所有文件 就可以了


## 查看日志

docker exec 命令允许您在 Docker 容器内运行命令。 以下命令行将在 mysql 容器中为您提供一个 bash shell：

```bash
$ docker exec -it mysql /bin/bash
mysql -uroot -p  123456 就进入mysql交互环境了
exit 退出mysql交互环境
exit 退出bin/bash
docker stop  容器id 退出守护进程 也就是不运行mysql了
```

MySQL Server日志可通过 Docker 的容器日志获得：

```bash
$ docker logs mysql
```

#用navicat 连接 docker启动的mysql 如果遇到 Authentication plugin ‘caching_sha2_password’ cannot be 。。。
$ docker exec -it mysql /bin/bash
再接着输入mysql -u root -p命令，然后输入自己的密码 123456
然后输入更新密码语句：ALTER USER ‘root’@’%’ IDENTIFIED WITH mysql_native_password BY ‘hvag’;
最后重启mysql  docker restart mysql
就可以连接了

“”“
这个错误出现的原因是在mysql8之前的版本中加密规则为mysql_native_password，而在mysql8以后的加密规则为

caching_sha2_password。

解决此问题有两种方法，一种是更新navicat驱动来解决此问题，

一种是将mysql用户登录的加密规则修改为mysql_native_password。

进行授权远程连接(注意mysql 8.0跟之前的授权方式不同)

授权

GRANT ALL ON *.* TO 'root'@'%';
刷新权限
flush privileges;
此时,还不能远程访问,因为Navicat只支持旧版本的加密,需要更改mysql的加密规则
3,更改加密规则
ALTER USER 'root'@'localhost' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER;
4,更新root用户密码
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456';
刷新权限
flush privileges;
OK，设置完成，再次使用 Navicat 连接数据库

## grant all privileges on *.*  to ‘root’@’%’ ;   给用于授予权限


GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'hvag' WITH GRANT OPTION;

”“”


通过[容器名字]或者[容器 ID]来重启 MySQL，让配置生效。

```bash
docker restart mysql
```

