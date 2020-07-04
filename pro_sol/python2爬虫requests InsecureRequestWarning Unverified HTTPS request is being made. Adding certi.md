## python2爬虫requests InsecureRequestWarning: Unverified HTTPS request is being made. Adding certi

```shell
import requests
requests.packages.urllib3.disable_warnings()
response = requests.get(url, verify=False)
```

