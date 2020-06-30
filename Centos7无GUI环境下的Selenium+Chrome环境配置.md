## Centos7无GUI环境下的Selenium+Chrome环境配置

```shell
yum install -y epel-release
yum install google-chrome-stable -y
yum install -y Xvfb libXfont xorg-x11-fonts*
```

**下载webdriver驱动**

```shell
#查看浏览器版本
google-chrome-stable -version
```

下载对应驱动：linux版本

https://npm.taobao.org/mirrors/chromedriver

```shell
#解压，需要安装 unzip
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin/   #移动到应用程序的可执行文件夹内
```

**测试**

```shell
from selenium import webdriver
option = webdriver.ChromeOptions()
option.binary_location = '/usr/bin/google-chrome-stable'
option.add_argument('--headless')
option.add_argument('--disable-gpu')
option.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=option)

driver.get('http://www.baidu.com')
print(driver.title)
```

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200630141000.png?raw=true)

输出为截图内容就成功了

------

[参考](https://www.jianshu.com/p/4592e83d9e81)

![](https://github.com/zyl-fun/pic/blob/master/%E6%88%91%E5%92%8C%E4%BD%A0%E5%A6%88%E5%A6%88%E4%BC%9A%E6%B0%B8%E8%BF%9C%E7%88%B1%E4%BD%A0.png?raw=true)