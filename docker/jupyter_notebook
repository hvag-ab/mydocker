## docker search base_notebook

## docker pull jupyter/base-notebook
docker pull jupyter/scipy-notebook

mkdir $HOME/nbs 创建nbs文件

后台运行
docker run -d --restart=always --name=jupyter -p 18888:8888 \
-v $HOME/nbs:/home/jovyan/ \
jupyter/scipy-notebook

docker exec -it jupyter /bin/bash 
进入内部后 然后用conda安装其他的包 conda install xxx
exit 退出内部
如果访问 localhost:18888 出现权限错误，可以使用 docker logs jupyter 来输出该容器的标准输出流，你可能看到一串类似 http://localhost:8888/?token=3c32ac9203dc507d0d6bbcc191c83c650c081308100eb397 的带 token 的 URL，将 8888 替换为我们的 18888 在浏览器中打开即可完成验证。

请注意 如果要读取文件的话
因为是docker环境 不能直接跟本机环境交互  需要放在挂载的文件里 或者 直接通过jupyter notebook home页 上传文件按钮上传文件就ok了