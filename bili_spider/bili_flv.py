import time

import requests

requests.packages.urllib3.disable_warnings()
import re
import json
import redis
from lxml import etree
headers = {
    # "Host":"api.bilibili.com",
    "Connection": "keep-alive",
    "Origin" : "https://www.bilibili.com",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Accept" : "*/*",
    "Referer" : "",
    "Accept-Encoding" : "gzip, deflate, br",
    "Accept-Language" : "zh-CN,zh;q=0.9",
    "Range" : "bytes:0--"
    # "Sec-Fetch-Dest" : "empty",
    # "Sec-Fetch-Mode" : "cors",
    # "Sec-Fetch-Site" : "cross-site"
}

#写入自己的cookie
cookies = {
    "_uuid" : "",
    "buvid3" : "",
    "SESSDATA" : "",
    "bili_jct" : "",
    "sid" : ""
}

#若没有代理则可以忽略
http_config = {
    "user": "",
    "pass": "",
    "concurrent": 100,
    "proxyServer": "http://http-proxy-t3.dobel.cn:9180",
    "type": "duobeiyun"
}
count = "//{}:{}".format(http_config['user'],http_config['pass'])
proxies = {
    "http": http_config['proxyServer'].replace('//', count + '@'),
    "https": http_config['proxyServer'].replace('//', count + '@')
}




def download(starturl):
    res = requests.get(url=start_url, verify=False, cookies=cookies)
    print(res.status_code)
    content = res.content.decode('utf-8')

    data = re.search(r'cid=(\d+)&aid=(\d+)&attribute=(\d+)&bvid=(\w+)', content)

    title = re.search(r'<title data-vue-meta="true">(.*?)_', content).group(1)
    title = title.replace(' ', "") + '.mp4'
    cid = data.group(1)
    avid = data.group(2)
    base_url = "https://api.bilibili.com/x/player/playurl?cid={}&avid={}&qn=80&otype=json&requestFrom=bilibili-helper".format(cid, avid)
    print(base_url)
    res = requests.get(headers=headers, url=base_url, verify=False, cookies=cookies).content
    headers['Referer'] = start_url
    res_json = json.loads(res)
    url = res_json['data']['durl'][0]["url"]
    print(url)



    with open(title,'ab') as f:
        f.write(requests.get(headers=headers, url=url,verify = False,cookies=cookies).content)
        f.flush()


if __name__ == '__main__':
    start_time = time.time()
    start_url = input('请输入URL：')
    start_url = start_url.replace(" ",'')
    download(start_url)
    print('总共花费{}秒'.format(time.time()-start_time))

