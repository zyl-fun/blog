# Linux命令行与shell脚本编程大全学习

## 什么是Linux

Linux内核 / GNU工具 / 图形化桌面环境 / 应用软件

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200623101843.png?raw=true)

内核负责

1. 系统内存管理
2. 软件程序管理
3. 硬件设备管理
4. 文件系统管理

**系统内存管理**

内核管理系统的虚拟内存和物理内存

通过硬盘上的存储空间来实现虚拟内存，称为交换空间



![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200623102827.png?raw=true)

**软件程序管理**

第一个进程 init 进程来启动其他进程

内核启动，把init加载到虚拟内存，内核在启动其他进程都会在虚拟内存给新进程分配一块专有的区域来存储该进程用到的数据和代码

ubuntu /etc/init.d

Linux操作系统有5个运行级别

运行级为 1 ，只启动基本的系统进程及一个控制台终端进程，单用户模式，用来在系统有问题进行紧急的文件维护

运行级 3 ，常见的黑窗口模式

运行级 5， 图形化操作界面

**硬件设备管理**

设备驱动代码

内核模块

**文件系统管理**

## GNU工具

处理文件的工具

操作文本的工具

管理进程的工具

**shell**

输入文本命令，解释命令，在内核中执行

除了 bash shell, Linux其他的shell

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200623105523.png?raw=true)

## 桌面环境

X Window / KDE桌面 / GNOME / Unity桌面

## Linux发行版

提供一站式的Linux安装，内核，桌面，预编译好的应用

**特定用途的Linux发行版**

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200623110342.png?raw=true)

## 走进shell

将虚拟控制台终端看作CLI

cat /etc/passwd 系统账户列表和每个用户的基本配置信息

**man命令**

man -k 关键字 查找与关键字相关的命令

man -k terminal

man -k net

**文件系统**

系统文件在根驱动器，用户文件在另一驱动器中

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200623113121.png?raw=true)

常见的目录名遵循 FHS http://www.pathname.com/fhs

## shell命令

**ls**

```shell
ls -l * [] !
ls -l --time=atime 文件 #显示文件的访问时间，默认是创建时间
ls -Fd #-d表示只列出目录本身的信息，不列出子目录信息
```

**创建文件**

```shell
touch
```

**复制文件**

```shell
cp -i(强制覆盖询问) 源文件 目标文件
cp -R 递归复制目录
```

**Linux硬链接和软链接**

参考：https://www.cnblogs.com/fengdejiyixx/p/10821820.html

硬链接和软链接

文件有文件名字和数据，在linux 分为用户数据和元数据
用户数据：文件数据块，记录文件真实内容的地方
元数据： 文件的附加属性（文件大小，创建时间，所有者等信息）

硬链接，inode节点号相同，当inode节点上的链接数减为0，inode节点和对应的数据块会被回收

软链接，都是文件名字，inode节点号不同，指向两个不同的数据块，A为B的软链接，A的数据块存放的是B的路径名
为主从关系，B被删除，软链接仍然存在，但是确实无效的

区别：
硬链接不能对目录创建，不能对不同的文件系统创建硬链接，不能对不存在的文件创建硬链接
软链接可以对目录创建，可以对不同的文件系统进行创建，可以对不存在的文件创建软链接

链接的源文件要写绝对路径

```shell
ln -s /root/zyl_code/my_python3.7/ls_test/111 111_link #创建软连接
ls -li #查看文件或目录的inode编号，若编号一直，则是同一个文件
#不加 s 创建硬链接
```

**重命名文件**

Linux重命名称为移动

```shell
mv 1 2 #重命名文件1，但是inode编号是不变的
mv -i #在覆盖现有的文件时，发出警告
```

**删除文件**

rm

**目录操作**

d开头说明是一个目录

```shell
mkdir -p docker/mysql/{conf,data} #在最后建立两个子文件夹
```















