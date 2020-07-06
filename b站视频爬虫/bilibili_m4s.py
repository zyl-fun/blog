import time

import requests

requests.packages.urllib3.disable_warnings()
import re
import json
import redis
from lxml import etree
import os

import subprocess
import imageio

#基本配置
video_headers = {
    # "Host":"cn-bj-lxix-bcache-05.bilivideo.com",
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


audio_headers = {
    # "Host":"upos-sz-mirrorhw.bilivideo.com",
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

#添加自己的cookie,尽量写全
cookies = {
    "_uuid" : "",
    "buvid3" : "",
    "SESSDATA" : "",
    "bili_jct" : "",
    "sid" : ""
}

http_config = {
    "user": "ZGZFHTT1",
    "pass": "gL0I092UHjf",
    "concurrent": 100,
    "proxyServer": "http://http-proxy-t3.dobel.cn:9180",
    "type": "duobeiyun"
}
count = "//{}:{}".format(http_config['user'],http_config['pass'])
proxies = {
    "http": http_config['proxyServer'].replace('//', count + '@'),
    "https": http_config['proxyServer'].replace('//', count + '@')
}




#开始下载
def download(start_url):

    video_headers['Referer'] = start_url
    audio_headers['Referer'] = start_url
    data = get_url(start_url)
    video_url = data['video_url']
    audio_url = data['audio_url']
    name = data['title']
    biaoshi = start_url.split('/')[-1]
    # print(biaoshi)
    video_name = biaoshi + '.mp4'
    audio_name = biaoshi + '.mp3'
    with open(video_name,'ab') as f:
        f.write(requests.get(headers=video_headers, url=video_url,verify = False,cookies=cookies).content)
        f.flush()
        # r = requests.get( url=test_url,verify = False,cookies=cookies)
        # print(type(r.__dict__['_content']))
    with open(audio_name, 'ab') as f:
        f.write(requests.get(headers =audio_headers, url=audio_url, verify=False, cookies=cookies ).content)
    merge(video_name,audio_name,name)
#获取下载url
def get_url(start_url):
    # cid = 189517917 & aid = 838066255 & attribute = 8404992 & bvid = BV17g4y167SZ & show_bv = 1

    res = requests.get(url=start_url,verify=False,cookies=cookies)
    print(res.status_code)
    content =res.content.decode('utf-8')

    data = re.search(r'cid=(\d+)&aid=(\d+)&attribute=(\d+)&bvid=(\w+)', content)
    # cid = data.group(1)
    # bvid = data.group(4)
    # print(cid,bvid)
    # base_url = re.search(r'audio(.*?)baseUrl":"(.*?)","base_url',content)
    # print(base_url.group(2))
    # json_url = "https://api.bilibili.com/x/player/playurl?cid=%s&fnver=0&fnval=16&type=&otype=json&bvid=%s" % (cid,bvid)
    # print(json_url)
    # res = requests.get(url=json_url,cookies=cookies,verify=False)
    # print(res.json())
    # data = res.json()
    # url_dict = {
    #     'video_url': data['data']['dash']['video'][0]["baseUrl"],
    #     'audio_url': data['data']['dash']['audio'][0]['baseUrl']
    # }
    # 贪婪匹配
    title = re.search(r'<title data-vue-meta="true">(.*?)_', content).group(1)
    title = title.replace(' ',"") + '.mp4'


    url_dict = {
        "video_url" : re.search(r'video(.*?)baseUrl":"(.*?)","base_url',content).group(2),
        "audio_url" : re.search(r'audio(.*?)baseUrl":"(.*?)","base_url',content).group(2),
        'title' : title
    }


    return url_dict
#合并视频和音频
def merge(video_name,audio_name,name):
    print(name)
    cmd = 'ffmpeg -i ' + video_name + ' -i ' + audio_name + ' -c copy ' +name
    print(cmd)
    subprocess.call(cmd, shell = True)
    os.remove(video_name)
    os.remove(audio_name)

if __name__ == '__main__':
    #注意，输入网址后需要空格一下再回车
    start_url = input("请输入URL:")
    start_url = start_url.replace(' ',"")
    start_time = time.time()

    download(start_url)
    print('下载完成，总共耗时{}秒'.format(time.time()-start_time))
    # get_url('https://www.bilibili.com/video/BV1ai4y1t7JA')