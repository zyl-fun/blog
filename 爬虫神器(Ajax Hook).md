## 爬虫神器(Ajax-Hook)爬取七麦数据

*爬取https://www.qimai.cn/rank/marketRank各app对应详情页链接*

https://raw.githubusercontent.com/wendux/Ajax-hook/master/dist/ajaxhook.min.js  把源码粘贴到控制台，执行

```shell
ah.proxy({
    //请求发起前进入
    onRequest: (config, handler) => {
        console.log(config.url)
        handler.next(config);
    },
    //请求发生错误时进入，比如超时；注意，不包括http状态码错误，如404仍然会认为请求成功
    onError: (err, handler) => {
        console.log(err.type)
        handler.next(err)
    },
    //请求成功后进入
    onResponse: (response, handler) => {
    	if (response.config.url.startsWith('https://api.qimai.cn/rank/index')) {
    		console.log('**************************************************')
            axios.post('https://39.107.46.92:8000/receiver/movie',{
                url:window.location.href,
                data:response.response
            })
        console.log(response.response)
        handler.next(response)
    	}  	
    }   
})
```

```javascript
var i = 0;
setInterval(function(){
	window.scrollTo(0, document.body.scrollHeight/1*i);   //1800为自定义滑动距离，当前代码为每秒向下滑动1/1800
	i++;
	console.log(i);
 }, 2000);  // 1000为间隔时间，单位毫秒
```

此时可以得到响应数据



