# docker-compose-jupyterlab



## How to use

## Change password

进入本地的pyton 解释器 首先本地的python必须安装了jupyterlab

```python3
$ python3 -c 'from notebook.auth import passwd; print(passwd())'
```
vim .env 
Change `ACCESS_TOKEN` in `.env`.

```sh
$ docker-compose up --build -d
```


## Update container

```sh
$ docker-compose stop
$ docker-compose build
$ docker-compose up
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

