## 解决github访问缓慢以及代码上传缓慢的问题

#### 修改hosts文件

本人使用 win10系统，需要修改下面文件夹中的hosts文件

```shell
C:\Windows\System32\drivers\etc
```

此文件可能无法保存修改，没有权限

右键hosts属性---------安全------编辑------添加------高级------立即查找-----选定自己登录时的账户或者选择 Everyone

两次确定后 ----------------权限选择完全控制------确定就可以了

#### 添加 IP

解决这个问题参考了两篇博客

http://tool.chinaz.com/dns/ 打开网址，输入 github.com

在查询列表中选择 TTL 值最小的 IP

之后在 hosts文件中添加就OK了

```shell
13.229.188.59 github.com
13.229.188.59 gist.github.com
13.229.188.59 github.global.ssl.fastly.net
13.229.188.59 nodeload.github.com
```

