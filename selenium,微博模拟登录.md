### selenium,微博模拟登录，关键词高级搜索

如果没有登录，不会显示高级搜索的按钮,需要进行模拟登录

模拟登录如果碰到验证码识别，则需要调用超级鹰打码平台

接口>>>>>>>>>>>>>>>>>>>>>>>>>>

```shell
https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D小米科技&page_type=user&page=1

https://m.weibo.cn/api/container/getIndex?containerid=100103type=3&q=小米科技有限公司&t=0&page_type=searchall&page=2

https://m.weibo.cn/api/container/getIndex?containerid=100103type=3&q=小米科技有限公司&t=0&page_type=searchall&page=3

https://weibo.com/u/6193644456
```







