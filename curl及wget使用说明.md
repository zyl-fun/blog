## curl的使用

注意：安装的时候可能会遇到报错，有可能是openssl没装，

```bash
apt install curl
apt install openssl
apt install openssl-dev
```

一些常用参数的用法

| 参数 | 说明                                | 示例                                                         |
| ---- | ----------------------------------- | ------------------------------------------------------------ |
| -A   | 设置user-agent                      | curl -A "Chrome" http://www.baidu.com                        |
| -X   | 用指定方法请求                      | curl -X POST http://httpbin.org/post                         |
| -I   | 只返回请求的头信息                  |                                                              |
| -d   | 以POST方法请求url，并发送相应的参数 | -d a=1 -d b=2 -d c=3<br />-d "a=1&b=2&c=3"<br />-d @filename |
| -O   | 下载文件并以远程的文件名保存        |                                                              |
| -o   | 下载文件并以指定的文件名保存        | curl -o fox.jpeg http://httpbin.org/image/jpeg               |
| -L   | 跟随重定向请求                      | curl -IL https://baidu.com                                   |
| -H   | 设置头信息                          | curl -o image.webp -H "accept:image/webp" http://httpbin.org/image |
| -k   | 允许发起不安全的SSL请求             |                                                              |
| -b   | 设置cookies                         | curl -b a=test http://httpbin.org/cookies                    |
| -s   | 不显示其他无关信息                  |                                                              |
| -v   | 显示连接过程中的所有信息            |                                                              |

自定义一个命令，查看本机外网IP

```
alias myip="curl http://httpbin.org/get|grep -E '\d+'|grep -v User-Agent|cut -d '\"' -f4"
```

## wget

安装：

```apt install wget```

参数说明

| A            | B                            | C                                             |
| ------------ | ---------------------------- | --------------------------------------------- |
| -O           | 以指定文件名保存下载的文件   | wget -O test.png http://httpbin.org/image/png |
| --limit-rate | 以指定的速度下载目标文件     | --limit-rate=200k                             |
| -c           | 断点续传                     |                                               |
| -b           | 后台下载                     |                                               |
| -U           | 设置User-Agent               |                                               |
| --mirror     | 镜像某个目标网站             |                                               |
| -p           | 下载页面中的所有相关资源     |                                               |
| -r           | 递归下载所有网页中所有的链接 |                                               |

```bash
# 镜像下载整个网站并保存到本地
wget -c --mirror -U "Mozilla" -p --convert-links http://docs.python-requests.org
```

## httpie

```bash
apt install httpie
pip install httpie
```

























