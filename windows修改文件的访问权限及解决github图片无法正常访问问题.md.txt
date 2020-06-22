在github上传图片发现图片无法正常加载出来

#### 修改hosts文件

本人使用 win10系统，需要修改下面文件夹中的hosts文件

```shell
C:\Windows\System32\drivers\etc
```

此文件可能无法保存修改，没有权限

右键hosts属性---------安全------编辑------添加------高级------立即查找-----选定自己登录时的账户或者选择 Everyone

两次确定后 ----------------权限选择完全控制------确定就可以了

#### 添加

在hosts文档中粘贴以下内容保存

```shell
# GitHub Start
140.82.114.4 github.com
140.82.114.4 gist.github.com
185.199.108.153 assets-cdn.github.com
151.101.64.133 raw.githubusercontent.com
151.101.108.133 gist.githubusercontent.com
151.101.108.133 cloud.githubusercontent.com
151.101.108.133 camo.githubusercontent.com
151.101.108.133 avatars0.githubusercontent.com
151.101.108.133 avatars1.githubusercontent.com
151.101.108.133 avatars2.githubusercontent.com
151.101.108.133 avatars3.githubusercontent.com
151.101.108.133 avatars4.githubusercontent.com
151.101.108.133 avatars5.githubusercontent.com
151.101.108.133 avatars6.githubusercontent.com
151.101.108.133 avatars7.githubusercontent.com
151.101.108.133 avatars8.githubusercontent.com 
# GitHub End
```

#### 参考

https://www.jianshu.com/p/25e5e07b2464



