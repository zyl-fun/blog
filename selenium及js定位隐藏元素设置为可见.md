### selenium及js定位隐藏元素设置为可见

找教程的过程一定要冷静，镇定，不要浮躁

参考------------>https://www.cnblogs.com/superhin/p/12604080.html

**豆果美食为例**

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200721164430.png?raw=true)



![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200721164514.png?raw=true)



python2环境

```pyth
# -*- coding: utf-8 -*-
import time

from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
option.add_argument('--no-sandbox')
option.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
driver = webdriver.Chrome(chrome_options=option)

driver.get("https://passport.douguo.com/login")
print(driver.title)

account = ''
pwd = ''

account_tag = driver.find_element_by_xpath(u"//input[contains(@placeholder,'手机号或邮箱')]")
# account_tag = driver.find_element_by_id('mail')
logtwo = driver.find_element_by_xpath("//div[contains(@class,'logtwo')]")
js = "arguments[0].setAttribute('style',arguments[1])"
style = "display:block"
driver.execute_script(js,logtwo,style)
account_tag.send_keys(account)
time.sleep(0.6)
pwd_tag = driver.find_element_by_xpath(u"//input[contains(@placeholder,'请输入密码')]")
# pwd_tag = driver.find_element_by_id('pwd')
pwd_tag.send_keys(pwd)
time.sleep(0.6)
login_tag = driver.find_element_by_xpath("//span[@id='mimalg']")
# login_tag = driver.find_element_by_id('mimalg')
login_tag.click()
time.sleep(1)
print(driver.title)
```

