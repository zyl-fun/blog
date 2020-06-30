## flask服务器支持https协议

本人只有服务器，没有购买域名，无法免费使用证书

自己生成证书，这个必须手动修改让浏览器支持，浏览器应该默认有安全警告，忽略就可以了

其次需要已经安装 openssl

```shell
openssl req -new -x509 -days 365 -nodes -out secret.pem -keyout secret.key
openssl pkcs8 -topk8 -inform PEM -outform PEM -in secret.key -out outfile.pem
```

```shell
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/test',methods=['GET'])
def receive():
    # res = request.form
    # print(res)


    return jsonify({'status':True})

if __name__ == '__main__':
	#注意证书的路径
    app.run(host='0.0.0.0',port=8000,debug=True, ssl_context=('secret.pem','secret.key'))
```

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200630094757.png?raw=true)

![](https://github.com/zyl-fun/pic/blob/master/%E6%88%91%E5%92%8C%E4%BD%A0%E5%A6%88%E5%A6%88%E4%BC%9A%E6%B0%B8%E8%BF%9C%E7%88%B1%E4%BD%A0.png?raw=true)