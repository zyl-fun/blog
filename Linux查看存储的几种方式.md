# Linux查看存储的几种方式

df命令会显示每个有数据的已挂载文件系统

```shell
df 
df -h #更加易读的方式
du命令显示某个特定目录（默认为当前目录）的磁盘使用情况
du -sh * | sort -nr #查看当前文件夹下的所有文件的大小及按其大小进行逆序排序
```

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200623151451.png?raw=true)

