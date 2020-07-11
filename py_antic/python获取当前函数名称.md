### python获取当前函数名称

我需要把程序内出错位置的错误信息和其所在执行函数的名称打印出来

我这样做

```python
            except Exception as e:
                fun_name = sys._getframe().f_code.co_name
                with open('coolapk_logs', 'a+') as f:
                    f.write(fun_name)
                    f.write('\n')
                    f.write(str(e))
                    f.write('\n')
```



