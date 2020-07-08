## B站视频爬虫-最新版（附代码）

### 第一种方法：fiddler + requests + ffmpeg

**（一）打开fiddler抓包工具，打开视频主页，点击播放，等待几秒，调整主体和内容类型（视频流一般比较大，而且为MP4格式），还需要把自己的cookies 记录下来**

![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706095231.png?raw=true)

![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706094146.png?raw=true)



![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706094610.png?raw=true)



**（二）点开一个，可以看到headers 等信息，查看 Request_Headers -----> raw**

```shell
GET /upgcxcode/39/28/196032839/196032839-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1594007037&gen=playurl&os=bcache&oi=3054633810&trid=e024d5c8ed96411a91a61e6eb1a54134u&platform=pc&upsig=aa5ccc731a2a18ca52bcb40cb6195a63&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&cdnid=3773&mid=602150709&orderid=0,3&agrr=0&logo=80000000 HTTP/1.1
Host: cn-bj-lxix-bcache-08.bilivideo.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
range: bytes=1923931-5072730
Accept: */*
Origin: https://www.bilibili.com
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.bilibili.com/video/BV19p4y1S7B6
Accept-Encoding: identity
Accept-Language: zh-CN,zh;q=0.9
```

注意参数有一个 range属性，因为整个视频是分段传输的，这个参数是规定每次请求多少字节的数据，此时查看响应头，也有range 参数，但是它多出一个总的字节数，这也是视频的总大小，我们把 range 改为 0 - max 就可以了，也可以写为 0-- 这样也是默认下载全部数据

![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706100243.png?raw=true)



把 headers 信息记录下来，写到代码里，如果按照这种方式，音频和视频是分开的，它们的头也有些不同，头需要分开写

**（三）使用 requests 库进行下载**

那么重要的一点来了，url来自哪里

在我们播放视频的时候，在视频播放完毕我们可以看到与众不同的接口

![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706131323.png?raw=true)

其实这对应的是它在播放完毕推荐列表的视频的接口

我们对其进行请求,会发现下载视频的链接和相对应的音频链接已经出现了

```shell
https://api.bilibili.com/x/player/playurl?cid=189517917&fnver=0&fnval=16&type=&otype=json&bvid=BV17g4y167SZ
```

![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706132645.png?raw=true)



其实这些信息在视频网页的源代码中都有体现，我们请求到这个页面，利用正则提取更好

![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706141553.png?raw=true)

![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706141607.png?raw=true)

![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706142229.png?raw=true)

**（四）对视频和音频进行合并**

[参考文章](https://blog.csdn.net/Tong_T/article/details/92794314)

[linux-ffmpeg下载安装](https://www.cnblogs.com/passedbylove/p/12166544.html)

利用 ffmpeg 进行音频和视频文件的合并

这里代码中有体现

*下载完成*

![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706165355.png?raw=true)

### 第二种方法：查阅资料，得知有个接口可以直接得到获取完整视频，有声音，格式为 .flv

```shell
https://api.bilibili.com/x/player/playurl?cid={}&avid={}&qn=80&otype=json&requestFrom=bilibili-helper
```

只要有 cid avid ，就可以拿到 URL

![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706165120.png?raw=true)

具体参照代码

### 对比

使用第一种方法

![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706175658.png?raw=true)

![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706175750.png?raw=true)

第二种办法

![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706175804.png?raw=true)

![](https://github.com/zyl-fun/pic/blob/master/bilibili_pic/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200706175817.png?raw=true)

哪个速度快，一眼便知

### 建议

建议使用 完美解码 打开视频，很强大的视频播放器

若此篇博客图片无法正常打开，请参照：[https://github.com/zyl-fun/blog/blob/master/%E8%A7%A3%E5%86%B3github%E8%AE%BF%E9%97%AE%E7%BC%93%E6%85%A2%E9%97%AE%E9%A2%98.md](https://github.com/zyl-fun/blog/blob/master/解决github访问缓慢问题.md)



### 参考

https://blog.csdn.net/ETalien_/article/details/102920579

https://www.52pojie.cn/thread-1209458-1-1.html

https://blog.csdn.net/Enderman_xiaohei/article/details/94718494

https://blog.csdn.net/Mike_Shine/article/details/81004136

------

![](https://github.com/zyl-fun/pic/blob/master/%E6%88%91%E5%92%8C%E4%BD%A0%E5%A6%88%E5%A6%88%E4%BC%9A%E6%B0%B8%E8%BF%9C%E7%88%B1%E4%BD%A0.png?raw=true)



