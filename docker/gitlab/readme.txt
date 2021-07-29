
一.进入容器 修改密码
docker exec -it <gitlabid> /bin/bash  


root@47:/# gitlab-rails console 
Loading production environment (Rails 4.2.10)

irb(main):001:0> user=User.where(id:1).first
=> #<User id:1 @root>

irb(main):002:0> user.password='12345678'
=> "123456"

irb(main):003:0> user.password_confirmation='12345678'
=> "123456"

irb(main):004:0> user.save!
Enqueued ActionMailer::DeliveryJob (Job ID: 86227e1d-cc49-44de-9179-e7c20a8b03f6) to Sidekiq(mailers) with arguments: "DeviseMailer", "password_change", "deliver_now", gid://gitlab/User/1
=> true
irb(main):005:0>
���ˣ�����Ա�û���������ϣ����ú������Ϊ12345678 �û���root

二.打开gitlab网站
url ： docker-compose.yml中 external_url 'http://172.17.111.237:8929' #若有域名可以写域名
登录： root   12345678
进入页面后 Menu - Projects - You projects 
填好信息后 点击Create a project 创建一个项目 
 
三.客户端 windows 下载git  mac linux 安装git
git bash中
$ ssh-keygen -t rsa -C 'xxx@xxx.com'
然后一路回车(-C 参数是你的邮箱地址)
$ cat ~/.ssh/id_rsa.pub 查看公匙

打开gitlab,找到Edit Profile-->SSH Keys--->Add SSH Key,并把上一步中复制的内容粘贴到Key所对应的文本框
粘贴完成后 点击 add key 按钮

回到gitlab页面点击Menu - Projects - You projects 
选择一个需要克隆的项目，进入 
点击按钮复制 clone with ssh 地址
新建一个文件夹，我在这里在我的电脑D盘下新建project文件夹
进入projects文件夹右键选择->Git Bash Here

设置用户名和邮箱

$ git config --global user.name "你的名字"
$ git config --global user.email "你的邮箱"

git clone 项目地址  会让你输入用户名(刚才设置的名字)

clone下来后 进入项目  新增一个文件 测试提交的文件.txt
git status 查看状态 如果你新增了文件 会提示那个文件
$ git add  测试提交的文件.txt
$ git commit -m "message"
$ git push origin main












