### linux安装python各种版本

[python各个版本大全](https://www.python.org/ftp/python/)

```bash
wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz  #下载
tar xJf Python-3.7.0.tar.xz   #解压

$ cd Python-3.7.0/
$ ./configure --with-ssl	# 配置openssl
$ make
$ make install

which python3.7 #查看位置
>>>/usr/local/bin/python3.7
```

#### 问题

linux环境python3出现pip is configured with locations that require TLS/SSL, however the..不可用的解决方法

首先明确问题出现原因，是因为openssl版本过低或者不存在 so：

1. 查看openssl安装包，发现缺少openssl-devel包 
   [root@localhost ~]# rpm -aq|grep openssl 
   openssl-0.9.8e-20.el5 
   openssl-0.9.8e-20.el5 
   [root@localhost ~]#
2. yum安装openssl-devel 
   [root@localhost ~]# yum install openssl-devel -y 
   查看安装结果 
   [root@localhost ~]# rpm -aq|grep openssl 
   openssl-0.9.8e-26.el5_9.1 
   openssl-0.9.8e-26.el5_9.1 
   openssl-devel-0.9.8e-26.el5_9.1 
   openssl-devel-0.9.8e-26.el5_9.1
3. 重新对python3.6进行编译安装，用一下过程来实现编译安装:

cd Python-3.6.4
./configure --with-ssl
make
sudo make install

------

ModuleNotFoundError: No module named '_ctypes'的解决方案

![image-20200805134326735](%E5%9B%BE%E7%89%87/image-20200805134326735.png)

yum install libffi-devel -y

------

![img](%E5%9B%BE%E7%89%87/u=228401719,2819682736&fm=173&s=6B62DC4FDC31049CF7B061B80300D012&w=640&h=360&img.JPEG)



