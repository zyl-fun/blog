# Linux-奇葩shell用法(后台模式)

```shell
sleep 5&
ps -f 
ps --forest
jobs
```

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200624114312.png?raw=true)

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200624114356.png?raw=true)

*把进程列表置于后台*

```shell
(sleep 2 ; echo $BASH_SUBSHELL ; sleep 2)&
(tar -cf shan.tar shan ; tar -cf shan2.tar shan)& #后台压缩
```

**协程**

协程可以在后台生成子shell,并在这个子shell执行命令

```shell
coproc sleep 10
#给自己的进程起名字
coproc my_sleep { sleep 10; }
coproc ( sleep 10; sleep 2 )
```



