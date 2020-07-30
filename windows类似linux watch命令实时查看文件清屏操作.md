### windows类似linux watch命令/实时查看文件/清屏操作

搜了搜，没找到好用的，用python写了个脚本

```py
import os
import time

#文件指针
zz = '0'
while 1:
    with open('tww_logs','r') as f:
        f.seek(int(zz))
        print(f.read())
        zz = f.tell()
    time.sleep(5)
    #下面这个是清屏操作
    # os.system('cls')


```

