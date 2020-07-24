### python+requests请求网络图片并以base64格式保存到json中

```python
import time
from gevent import monkey;monkey.patch_all()

from decimal import Decimal
from urllib.parse import quote
from io import BytesIO
import gevent

import requests
import re
import json
import redis
from lxml import etree
import threading
import sys
import os

conn = redis.Redis(host="",db=0, port=,password="")

import base64

def jin():
    url = "http://p18.qhimg.com/t01aec2530f64d9b9d6.png"
    res = requests.get(url=url)
    base64_data = base64.b64encode(res.content).decode()
    data = {
        'avatar':base64_data
    }

    conn.lpush('000_test',json.dumps(data))

def out():
    data = conn.rpop("000_test")
    data = json.loads(data)
    image_data = base64.b64decode(data['avatar'])
    with open('003.png','wb') as f:
        f.write(image_data)
if __name__ == '__main__':
    jin()
    out()
```

