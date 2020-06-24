# Linux-进程列表

```shell
pwd ; ls ; ls -lF
#连续执行多条命令
#如果想要成为进程列表，需要把这些命令包含在括号内
(pwd ; ls ; ls -lF ; echo $BASH_SUBSHELL)
#最后是查看是否生成子shell
```

加上括号让命令列表变为进程列表，生成子shell执行对应的命令

