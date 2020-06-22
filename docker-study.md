*参考文档*

[https://github.com/jackfrued/Python-100-Days/blob/master/Day91-100/92.Docker%E5%AE%B9%E5%99%A8%E8%AF%A6%E8%A7%A3.md](https://github.com/jackfrued/Python-100-Days/blob/master/Day91-100/92.Docker容器详解.md)

# 简介

基于GO语言开发

打包应用及应用的依赖到一个可移植的容器上

将应用程序和其依赖打包在一个文件里面，运行生成虚拟容器，程序在虚拟容器里面运行

用途：

提供一次性的环境

提供弹性的云服务

实践微服务框架



容器是不值得保留的，数据是非常重要的

# 安装

 https://www.runoob.com/docker/ubuntu-docker-install.html 

## 知识点

uname -r 查看自己操作系统的内核版本

linux 启动 docker服务 service docker start/stop/reload/status

netstat -ntlp 查看网络端口的使用状况

redis-cli shutdown 停止掉Redis服务

**sftp传文件**

sftp root@39.107.46.92

**查看信息和版本**

docker version

docker info

**查看所有镜像文件**

docker images

**删除镜像**

docker rmi 镜像ID

**通过镜像文件创建并运行容器**

docker container run --name mycontainer hello-world

**删除容器**

docker container rm mycontainer

# 使用Docker

## Nginx

```
docker pull nginx:latest 拉取镜像文件从云服务器中
docker run -d -p 80:80 --name zylnginx nginx + --rm 容器停止后自动自己
docker ps 查看运行中的容器
docker stop zylnginx 停止正在运行的容器
docker container ls -a 查看所有的容器
docker start zylnginx 启动容器
docker rm -f zylnginx 删除容器
```

### 前端页面映射到容器

```
docker exec -it zylnginx /bin/bash
exit 退出
```

把外部文件部署到容器中

```
docker run -d -p 80:80 -v /root/html:/usr/share/nginx/html --name mynginx nginx #数据卷操作
```

## Redis

```
docker pull redis
pkill redis 杀死原来存在的redis进程
docker run -d -p 6379:6379 --name zylredis-master redis
```

**改端口/指定口令/持久化方式**

```
docker run -d -p 6379:6379 --name zylredis redis redis-server --requirepass 199802 --port 6379 --appendonly yes
```

**主从热备**

```
读写分离
主库写，从库读

查看容器IP地址
docker inspect --format '{{ .NetworkSettings.IPAddress }}' 82ce64b0e7bf
容器之间可以通过IP进行互通，也可以使用网络别名

创建从库-进行互联
docker run -d -p 6380:6379 --link zylredis-master:zylredis-master --name redis-slave-1 redis redis-server --slaveof zylredis-master 6379 --masterauth 199802

docker run -d -p 6381:6379 --link zylredis-master:zylredis-master --name redis-slave-2 redis redis-server --slaveof zylredis-master 6379 --masterauth 199802

redis查看从库
info replication
```

flush db 清除 Redis 缓存

## MySQL

```
需要设置口令才能连接数据库
需要把主机的mysql服务停掉
docker run -d -p 3306:3306 --name zylmysql -e "MYSQL_ROOT_PASSWORD=123" mysql:5.7.29 

mysql -u root -p 连接数据库
select version() 查看数据库版本

测试，建立测试数据库文件夹
mkdir -p docker/mysql/{conf,data}

保留数据 数据卷操作 映射数据和数据库配置
docker run -d -p 3306:3306 -v /root/docker/mysql/conf:/etc/mysql/mysql.conf.d -v /root/docker/mysql/data:/var/lib/mysql --name zylmysql -e "MYSQL_ROOT_PASSWORD=123456" mysql:5.7.29 
```

# 使用Docker构建自己的镜像

**第一种**

```shell
docker commit 1be9408ed6b9 zyl/zylmysql
docker run -d -p 3306:3306 --name zylmysql zyl/zylmysql

打包
docker save zyl/zylmysql -o mysql.tar
加载
docker load -i mysql.tar
```

**第二种，将镜像上传服务器**

```
登录
docker login

上传镜像
docker push zyl/zylmysql

```

**第三种 dockerfile 构建镜像**

*Flask*

```
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r'/api/*':{'origins': '*'}})
api = Api(app)

class Product(Resource):
    def get(self):
        products = ['Ice Cream', 'Chocolate', 'Coca Cola', 'hamburger']
        return {'products': products}

api.add_resource(Product, '/api/products')
```

把依赖项整理出来

https://blog.csdn.net/weixin_44038167/article/details/102968480

```
flask
flask-restful
flask-cors
gunicorn
```

服务器启动项文件

start.sh

```
#!/bin/bash
exec gunicorn -w 4 -b 0.0.0.0:8002 app:app
```

构建镜像

在 shell 中写代码时空格键和制表符千万不要混用

```
touch Dockerfile
```

```
#指定基础镜像
FROM python:3.7
#指定镜像维护者
MAINTAINER zyl "zylandstt@qq.com"
#把文件添加到容器中指定的位置
ADD api/* /root/api/
#设置工作目录
WORKDIR /root/api
#安装依赖
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple/
#容器启动执行的命令
ENTRYPOINT ["./start.sh"]
#端口
EXPOSE 8002
```

创建镜像

```
docker build -t "zyl/myapp" .
```

运行容器

```
docker run -d -p 8002:8002 --name myapp zyl/myapp 
```

查看日志

https://www.cnblogs.com/mr-wuxiansheng/p/11412489.html

```
docker logs --since 30m
```



# 多容器管理

**Kubernetes(K8S)**