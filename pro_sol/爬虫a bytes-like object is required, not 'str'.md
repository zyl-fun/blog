### 爬虫a bytes-like object is required, not 'str'

requests 拿请求到的 content 时出现这种错误

python2一般不会出现这种情况

因为python2设置了

```pyth
#*encoding=utf-8
```

python3需要decode

```pytho
res = requests.get(url=url, headers=headers, cookies=cookies, verify=False)
html_content = res.content.decode('utf-8')
```

