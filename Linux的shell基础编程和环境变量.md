# Linux的shell基础编程和环境变量

## shell

```shell
shell 的交互方式
后缀一般是.sh
开头为#!/bin/bash
为脚本添加可执行权限 chmod
./脚本名字
如果不想用上面那种方法执行脚本，可以把脚本所在的目录的绝对路径加到系统的环境变量里，这样比较方便
```

```py
#! /bin/bash
for FRUIT in apple banana pear; do
	echo "I like $FRUIT"
done
```

```shell
I like apple
I like banana
I like pear	
```

**输入两个整数，计算从m到n整数的求和结果**

```shell
printf 'm ='
read m
printf 'n ='
read n
a=$m
sum=0
while [ "$a" -le "$n" ];
do
        sum=$[ sum + a ]
        a=$[ a + 1 ]
done
echo '结果：'$sum
```

**验证密码的脚本**

必须是双引号

```shell
printf '请输入密码：'
read key
secret=199802
while [ "$key" != "$secret" ];
do
	echo '密码错误，请再试一次'
	read key
done
echo '验证通过'
```

![](https://github.com/zyl-fun/pic/blob/master/%E6%88%91%E5%92%8C%E4%BD%A0%E5%A6%88%E5%A6%88%E4%BC%9A%E6%B0%B8%E8%BF%9C%E7%88%B1%E4%BD%A0.png?raw=true)



