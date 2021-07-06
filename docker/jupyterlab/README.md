# docker-compose-jupyterlab



## How to use

## Change password

1 首先本地的python必须安装了jupyterlab 
2 bash运行 然后输入密码（记住密码后面登录jupyterlab会让输入密码） 然后会生成加密字符串
```python3
$ python3 -c 'from notebook.auth import passwd; print(passwd())'
```
3 修改.env中的 加密字符串
vim .env 
ACCESS_TOKEN=加密字符串

```sh
$ docker-compose up --build -d
```


## Update container

```sh
$ docker-compose stop
$ docker-compose build
$ docker-compose up -d
```

为了方便管理，讲服务加入systemctl管理：
 # /usr/lib/systemd/system/jupyter.service 
 
[Unit] 
Description=Jupyter Management 
After=network.target  
 
[Service] 
User=root
Group=root
WorkDirectory=/anaconda 
ExecStart=/usr/local/bin/jupyter lab  

Restart=on-failure
RestartSec=10

 
[Install] 
WantedBy=multi-user.target
 
 启动：
 $ systemctl daemon-reload 
 $ systemctl start jupyter 
开机启动
 $ systemctl enable jupyter

