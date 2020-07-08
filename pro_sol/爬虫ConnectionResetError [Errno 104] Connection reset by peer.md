### 爬虫ConnectionResetError: [Errno 104] Connection reset by peer

我的问题我使用 requests库进行请求，可能是没有限制频率睡眠，导致出错

**我的解决办法**

```py
            for i in range(5):
                try:
                    res = requests.get(url,headers = headers)
                    url = res.url
                    if '/in/' in url:
                        global page_num
                        page_num += 1
                        # per_url_list.append(url)
                        print(url)
                        person_info(url)
                    break


                except Exception as e:
                    print(e)

                    if i < 5:
                        time.sleep(0.5)
            time.sleep(0.2)
```

一次请求不成功，就多请求几次，并且设置睡眠