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

------

https://github.com.ipaddress.com/  找到对应的IP地址

```shell
140.82.114.4 github.com
140.82.114.4 github.global.ssl.fastly.net
```

添加到hosts文件中

------

http://tool.chinaz.com/dns/ 打开网址，输入 github.com

在查询列表中选择 TTL 值最小的 IP

之后在 hosts文件中添加就OK了

```shell
13.229.188.59 gist.github.com
13.229.188.59 nodeload.github.com
```

最后 命令行

```shell
ipconfig /flushdns
```

#### 补充-图片不能正常显示问题

https://www.ipaddress.com/

浏览器控制台检查是哪个网址链接坏掉

访问上面这个网站，并且输入，之后把IP添加到hosts文件中即可

#### 2020年8月5日更新

最近解决方式，浏览器控制台复制失败的域名，

```shell
raw.githubusercontent.com
```

访问 http://tool.chinaz.com/dns/

选择 TTL 最小的 IP,更新到 hosts 文件

```shell
ipconfig /flushdns
```

亲测有效

