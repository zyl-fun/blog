## centos python3.7 No module named '_bz2'

```shell
yum install bzip2-devel
curl -O https://github.com/zyl-fun/pic/blob/master/mybook/_bz2.cpython-37m-x86_64-linux-gnu.so
//wget 也可以
find / -name lib-dynload
//找到父文件夹为python3.7的路径
//将上面下载好的文件复制到找到的文件路径
chmod +x _bz2.cpython-37m-x86_64-linux-gnu.so
```

![](https://github.com/zyl-fun/pic/blob/master/%E6%88%91%E5%92%8C%E4%BD%A0%E5%A6%88%E5%A6%88%E4%BC%9A%E6%B0%B8%E8%BF%9C%E7%88%B1%E4%BD%A0.png?raw=true)



