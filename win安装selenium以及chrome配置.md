### win安装selenium以及chrome配置

**安装selenium**

本人使用 pipenv包管理工具

```shell
pipenv install selenium
```

**下载浏览器驱动**

```shell
chrome://version/ #查看浏览器版本
http://npm.taobao.org/mirrors/chromedriver/ #找到对应版本
pipenv --venv #查看python环境目录，将下载好的 chrome.exe 文件拷贝到Scripts文件夹下
```

**测试**

```py
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
```