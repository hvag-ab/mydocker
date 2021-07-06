## Whether to allow the user to run the notebook as root.
c.NotebookApp.allow_root = True

c.NotebookApp.ip = '*'

c.NotebookApp.port = 8888
# jupyter工作目录，所有在jupyter创建的文件都会保存到这里
c.NotebookApp.notebook_dir = '/anaconda'

# 允许远程访问
c.NotebookApp.allow_remote_access = True

c.NotebookApp.enable_mathjax = True # 启用 MathJax

# 禁止用host的浏览器打开jupyter
c.NotebookApp.open_browser = False

# 允许所有的ip都能访问 否则日志会出现跨域错误 不被允许
c.NotebookApp.allow_origin = '*'

# nginx代理的时候 location /jupyter
#c.NotebookApp.base_url = 'jupyter'

#c.NotebookApp.token = 'myTokenPswrd'
