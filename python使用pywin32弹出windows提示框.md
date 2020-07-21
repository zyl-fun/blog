### python使用pywin32弹出windows提示框

```shell
import win32con
import win32api
url_list = []
if not url_list:
    win32api.MessageBox(0, '更换cookie', '警告！！！！', win32con.MB_OK)
```

