### 参考网站

[https://github.com/jackfrued/Python-100-Days/blob/master/Day31-35/31-35.%E7%8E%A9%E8%BD%ACLinux%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F.md](https://github.com/jackfrued/Python-100-Days/blob/master/Day31-35/31-35.玩转Linux操作系统.md)

https://man.linuxde.net/

### 端口占用情况

```
netstat -nulpt | grep 端口号
```

```
losf -i :端口号 #端口号前面对应的ip地址，没有的话 空格占位

#杀死进程
kill -9 进程ID
```

### 查看进程pid

```
ps -ef | grep pycharm
ps -aux | grep pycharm
```

ps aux 查看所有在运行的进程

ps -ef 

### 查看存储情况

df -i

df -Ht

### Linux解压缩

https://blog.csdn.net/weixin_44038167/article/details/103530907

### 文件操作

[http://39.107.46.92/jqxx/2.linux%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.pdf](http://39.107.46.92/jqxx/2.linux常用命令.pdf)

**找出从名为access.log日志文件访问数量最大的IP地址和访问的次数**

```
tail -100000 access.log | awk '{print $1}' | sort | uniq -c | sort -nr 
```

**找出最常用的10条命令**

```
history | awk "{print $2}" | sort | uniq -c | sort -n -r -k 1 | head -n 10
```

### 查看 cpu个数

```
cat /proc/cpuinfo | grep processor | wc -l
```

### scp && sftp

```
sftp root@39.107.46.92

scp -r api root@120.77.222.217:/root/examples/example02/
```

### host操作

hostname 查看主机名

hostnamect set-hostname <your-name> 修改主机名

修改host 配置文件，节点之间可以通过 hostname 互相访问 vim /etc/hosts   ip hostname

### 清除Linux命令行历史命令记录

history -c

### ssh

```shell
 ssh -p 22 root@39.107.46.92
```

### grep零言断宽&正则表达式

https://blog.csdn.net/weixin_33708432/article/details/92195888?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase

### 终端xargs

https://www.runoob.com/linux/linux-comm-xargs.html

### pip 指定下载源

-i http://pypi.douban.com/simple --trusted-host pypi.douban.com 

### alias 

省略代码提交的繁琐步骤，个人使用

```python
alias tj='git add .;git commit -m "commit";git push -u origin master'
```

**注意等号两边是不可以有空格的**

### 每隔指定时间查看指定文件的大小

```python
watch -d- n 秒数 du -sh 文件夹
```



![](https://github.com/zyl-fun/pic/blob/master/%E6%88%91%E5%92%8C%E4%BD%A0%E5%A6%88%E5%A6%88%E4%BC%9A%E6%B0%B8%E8%BF%9C%E7%88%B1%E4%BD%A0.png?raw=true)