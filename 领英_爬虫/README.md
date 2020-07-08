## 领英爬虫 python+requests+selenium

利用 selenium 百度搜索定位公司员工的个人主页，根据拿到的个人主页链接，使用requests获取页面，再利用正则解析需要的数据

*由于正则规则写起来很麻烦，只对姓名和大学进行了提取，思路有了，真正需要信息的时候，再进行正则规则的定义就可以了*

最后保存在 xlsx 文件之中

![](https://github.com/zyl-fun/blog/blob/master/%E9%A2%86%E8%8B%B1_%E7%88%AC%E8%99%AB/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200708170228.png?raw=true)



![](https://github.com/zyl-fun/blog/blob/master/%E9%A2%86%E8%8B%B1_%E7%88%AC%E8%99%AB/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200708170322.png?raw=true)





**代码里设置了睡眠，保证稳定性，速度可能没有那么快，有些人的大学匹配规则是不同的，解析规则可能没有写全，有些人主页也可能并没有大学**

**cookie需要改为自己的cookie,要写完整**

![](https://github.com/zyl-fun/pic/blob/master/%E5%BC%80%E4%BC%9A.png?raw=true)

