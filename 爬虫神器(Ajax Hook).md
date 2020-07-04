## Ajax-Hook爬取七麦数据

[参考](https://mp.weixin.qq.com/s?__biz=MzAwNDc0MTUxMw==&mid=2649644252&idx=1&sn=a698dfa8f024d24acba02be1253a5728&chksm=833dbc3ab44a352c8c4f39a6a184662115d565d9a9488f062ddecbb8103d0f361d5dc6a76b41&xtrack=1&scene=90&subscene=93&sessionid=1592883891&clicktime=1592883893&enterid=1592883893&ascene=56&devicetype=android-29&version=27000f3f&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&exportkey=AzbNcsTaAdhETJXvPdbdUPA%3D&pass_ticket=tdpzoo65km8yEXy38BvyUemjGvVsDUG8VTSFP5AR%2BgQ%3D&wx_header=1)

*爬取https://www.qimai.cn/rank/marketRank各app对应详情页链接*

本人尝试使用 selenium 及 参考大神们的 js逆向解密，但失败了，于是配合 ajax-hook在浏览器控制台直接进行接口数据抓取，再利用 axios 发送到后端 flask 服务器 

- [ ] 利用 ajax-hook，[ajax-hook 源码地址](https://raw.githubusercontent.com/wendux/Ajax-hook/master/dist/ajaxhook.min.js)
- [ ] axios发送数据 [axios源码地址](https://unpkg.com/axios@0.19.2/dist/axios.min.js)
- [ ] 在浏览器控制台利用 js 脚本模拟下拉

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

**已经把上面所有代码封装到一个 js 文件**

使用,忽略上面，把下面代码粘贴到控制台即可

```shell
var script = document.createElement('script');
script.src = "https://cdn.jsdelivr.net/gh/zyl-fun/pic@v1.0.1/mybook/hook.js";
document.getElementsByTagName('head')[0].appendChild(script);
```

```shell
hook.js 爬取苹果
hooka.js 不访问服务器
hook-zh.js 中国应用商店app
```

**后端服务器代码**

```shell
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import redis
r = redis.Redis(host="",password="",port=6379, db=0)
print(r)

time_tup = time.time()

ctime = '%.1f' % time_tup


app = Flask(__name__)
CORS(app)
@app.route('/receiver/movie',methods=['POST'])
def receive():
    # res = request.form
    # print(res)

    content = json.loads(request.data)
    print(type(content))
    data = json.loads(content['data'])
    # print(type(data['rankInfo']))
    print(data)

    # for app in data['list']:
    #     appName = app['appInfo']['appName']
    #     companyName = app['appInfo']['publisher']
    #     print(appName,companyName)
    try:
        for app in data['rankInfo']:
            appName = app['appInfo']['appName']
            companyName = app['company']['name']
            print(appName, companyName)
            # print(type(appName),type(companyName))
            if appName:
                redis_data = {
                    "spider_config": {
                        "city": "all",
                        "task_type": "aldmin",
                        "job_type": "details",
                        "channel": "aldmin",
                        "type": "sell"
                    },
                    "data": {
                        "response_code": {
                            "": ""
                        },
                        "source_url": "",
                        "app_name": appName,
                        "company_name": companyName,
                        "url_crc": "",
                        "min_name":""
                    },
                    "ctime": ctime
                }
                r.lpush('qimaishuju',json.dumps(redis_data))
    except Exception as e:
        print(e)

    return jsonify({'status':True})



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True, ssl_context=('secret.pem','secret.key'))
```

------



![](https://github.com/zyl-fun/pic/blob/master/%E6%88%91%E5%92%8C%E4%BD%A0%E5%A6%88%E5%A6%88%E4%BC%9A%E6%B0%B8%E8%BF%9C%E7%88%B1%E4%BD%A0.png?raw=true)



