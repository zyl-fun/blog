之前学习一直使用国内的码云代码提交平台，今天开始在github更新自己的学习记录

### 建立自己的代码仓库

github的注册不必赘述

1. 首先在hub新建一个自己的仓库，如果是新注册的账户会自动提示你创建
2. git init
3. git remote add origin https://github.com/zyl-fun/blog.git（这是你自己的远程仓库的地址）
4. git add .
5. git commit -m '写上自己的提交说明'
6. git push -u origin master
7. git pull 从远端服务器拉取代码

### 设置免密提交

**生成公钥对**

```shell
cd #到家目录
ssh-keygen -t rsa -C "输入你创建github账号时绑定的邮箱" #连续回车
cd .ssh
ls #查看
cat id_rsa.pub #这个为公钥 复制其内容
```

**将公钥添加到github服务器**

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_1592805438701.png?raw=true)

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200622135757.png?raw=true)