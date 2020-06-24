## Linux环境变量

bash shell用一个叫作环境变量（environment variable）的特性来存储有关shell会话和工作环 境的信息（这也是它们被称作环境变量的原因）。这项特性允许你在内存中存储数据，以便程序 或shell中运行的脚本能够轻松访问到它们。这也是存储持久数据的一种简便方法。 

系统环境变量基本上都是使用全大写字母，以区别于普通用户的环境变量。 

```shell
env
printenv
```

全局环境变量可用于进程的所有子shell。 

查看局部环境变量的列表有点复杂。遗憾的是，在Linux系统并没有一个只显示局部环境 变量的命令。set命令会显示为某个特定进程设置的所有环境变量，包括局部变量、全局变量 以及用户定义变量。 

```shell
set
```

*设置用户自定义变量*

```shell
echo $zyl
zyl=888
echo $zyl
echo $zzz
zzz="zyl uuu"
echo $zzz
```

记住，变量名、等号和值之间没有空格，这一点非常重要。如果在赋值表达式中加上了空格， bash  shell就会把值当成一个单独的命令

*设置全局环境变量*

先创建局部环境变量，再导入到全局环境变量

修改子shell中全局环境变量并不会影响到父shell中该变量的值。 

*删除环境变量*

unset

在涉及环境变量名时，什么时候该使用$，什么时候不该使用$，实在让人摸不着头脑。 记住一点就行了：如果要用到变量，使用$；如果要操作变量，不使用$

在子shell中删除全局变量后，你无法将效果反映到父shell中。 

### 默认的shell环境变量

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200624151133.png?raw=true)

除了默认的Bourne的环境变量，bash shell还提供一些自有的变量，如表6-2所示。 

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200624151414.png?raw=true)

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200624151423.png?raw=true)

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200624151443.png?raw=true)

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200624151456.png?raw=true)

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200624152058.png?raw=true)

### PATH环境变量

PATH环境变量定义了用于进行命令和程序查找的目录

如果命令或者程序的位置没有包括在PATH变量中，那么如果不使用绝对路径的话，shell是没 法找到的。如果shell找不到指定的命令或程序，它会产生一个错误信息： 

```shell
-bash: hhh: command not found
```

问题是，应用程序放置可执行文件的目录常常不在PATH环境变量所包含的目录中。解决的 办法是保证PATH环境变量包含了所有存放应用程序的目录。 

可以把新的搜索目录添加到现有的PATH环境变量中，无需从头定义。PATH中各个目录之间是用冒号分隔的。你只需引用原来的PATH值，然后再给这个字符串添加新目录就行了。

```shell
 echo $PATH 
 PATH=$PATH:/home/christine/Scripts 
```

 如果希望子shell也能找到你的程序的位置，一定要记得把修改后的PATH环境变量导出。 

程序员通常的办法是将单点符也加入PATH环境变量。该单点符代表当前目录

```shell
 PATH=$PATH:. 
```

对PATH变量的修改只能持续到退出或重启系统。这种效果并不能一直持续。

### 系统环境变量

/etc/profile文件是系统上默认的bash shell的主启动文件。系统上的每个用户登录时都会执行 这个启动文件。 

/etc/profile文件是bash shell默认的的主启动文件。只要你登录了Linux系统，bash就会执行 /etc/profile启动文件中的命令。不同的Linux发行版在这个文件里放了不同的命令

*$HOME*

剩下的启动文件都起着同一个作用：提供一个用户专属的启动文件来定义该用户所用到的环 境变量。大多数Linux发行版只用这四个启动文件中的一到两个： 

 $HOME/.bash_profile 

 $HOME/.bashrc 

 $HOME/.bash_login 

 $HOME/.profile 

注意，这四个文件都以点号开头，这说明它们是隐藏文件（不会在通常的ls命令输出列表中 出现）。它们位于用户的HOME目录下，所以每个用户都可以编辑这些文件并添加自己的环境变 量，这些环境变量会在每次启动bash shell会话时生效。

shell会按照按照下列顺序，运行第一个被找到的文件，余下的则被忽略： 
$HOME/.bash_profile $HOME/.bash_login $HOME/.profile 注意，这个列表中并没有$HOME/.bashrc文件。这是因为该文件通常通过其他文件运行的。 

$HOME表示的是某个用户的主目录。它和波浪号（~）的作用一样。 

**交互式shell进程**

如果你的bash shell不是登录系统时启动的（比如是在命令行提示符下敲入bash时启动），那 么你启动的shell叫作交互式shell。交互式shell不会像登录shell一样运行，但它依然提供了命令行 提示符来输入命令。 

如果bash是作为交互式shell启动的，它就不会访问/etc/profile文件，只会检查用户HOME目录 中的.bashrc文件。 

**非交互式shell**

系统执行shell脚本时用的就是这种shell。不同的地方在于它 没有命令行提示符。

bash shell提供了BASH_ENV环境变量。当shell启动一个非交互式shell进 程时，它会检查这个环境变量来查看要执行的启动文件。如果有指定的文件，shell会执行该文件 里的命令，这通常包括shell脚本变量设置。

**环境变量持久化**

在大多数发行版中，存储个人用户永久性bash shell变量的地方是$HOME/.bashrc文件。这一 点适用于所有类型的shell进程

**数组变量**

```shell
mytest={one two three}
echo $mytest
echo ${mytest[1]}
echo ${mytest[*]}
mytest[2]=seven #改变索引的位置
unset 删除值
```



![](https://github.com/zyl-fun/pic/blob/master/%E9%A3%9F%E5%B1%8E%E5%95%A6%E4%BD%A0.gif?raw=true)