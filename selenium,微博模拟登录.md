### selenium,微博模拟登录，关键词高级搜索

#### 基础

如果没有登录，不会显示高级搜索的按钮,需要进行模拟登录

模拟登录如果碰到验证码识别，则需要调用超级鹰打码平台

接口

```shell
https://m.weibo.cn/api/container/getIndex?containerid=100103type=3&q=小米科技有限公司&t=0&page_type=searchall&page=3
```



type改为61，则显示为实时新闻，type=3则显示用户

登录 https://login.sina.com.cn/signup/signin.php

页面 https://weibo.com/u/6040538800

手机版 https://m.weibo.cn/

#### 问题

处理显示通知弹窗

https://www.cnblogs.com/vigogogogo/p/12922762.html

------

selenium无头模式定位不到元素

------

