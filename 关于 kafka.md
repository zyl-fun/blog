### 关于 kafka

------

#### 下载

链接：https://pan.baidu.com/s/1RKTD807egx4oPwocMX0mig 
提取码：w5s9 
复制这段内容后打开百度网盘手机App，操作更方便哦



案例 https://github.com/muscledreamer/Kafka_Demo/tree/master/KfkClient_pykafka

信息消费 https://www.kingname.info/2020/03/23/how-kafka-consume/



为什么学习 kafka https://www.kingname.info/2019/12/14/use-kakfa-in-spider/



使用python读写kafka https://www.kingname.info/2020/03/23/operate-kafka-by-python/

注意 不要安装 kafka库， 要安装 kafka-python,亲自踩坑，反复横跳

参考文章的代码有个地方需要注意

![image-20200804185613747](%E5%9B%BE%E7%89%87/image-20200804185613747.png)

要写成列表的形式



win10安装kafkahttps://blog.csdn.net/github_38482082/article/details/82112641

需要注意，路径一定不要太长，我直接放在 c盘下 C:\kafka_2.12-2.5.0

路径太长在启动服务的时候会报错，亲自踩坑

![image-20200804154857446](%E5%9B%BE%E7%89%87/image-20200804154857446.png)

出现 binding to port 则表示 zookeeper启动成功



![image-20200804154959795](%E5%9B%BE%E7%89%87/image-20200804154959795.png)

但是测试中文为什么无法被消费者接收到，待解答



 WARN Exception causing close of session 0x0: Unreasonable length = 1919902837 (org.apache.zookeeper.server.NIOServerCnxn)



 raise Errors.UnrecognizedBrokerVersion()
kafka.errors.UnrecognizedBrokerVersion: UnrecognizedBrokerVersion



python2 python3 的坑

kafka  kafka-python的安装切换

本人使用 pipenv 出现了bug



 self._sslobj.do_handshake()
OSError: [Errno 0] Error

------

**使用的基本流程**

```shell
.\bin\windows\zookeeper-server-start.bat  .\config\zookeeper.properties
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

my_pro生产者

```shell
import json
import os
import  time
import datetime

import kafka


producer = kafka.KafkaProducer( bootstrap_servers=["localhost:9092"], value_serializer = lambda m:json.dumps(m).encode())

for i in range(100):
    data = {
        "num":i,
        "ts":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    }
    producer.send("howtousekafka", data)
    time.sleep(1)
```

my_con消费者

```shell
import kafka
consumer = kafka.KafkaConsumer("howtousekafka",bootstrap_servers=["localhost:9092"],group_id = "test_2",auto_offset_reset='earliest')
for msg in consumer:
    print(msg.value)
```

#### 微博的使用

关键词生产者，关键词很多

一个生产者可以依次爬取多个关键词对应的最新消息，一个消费者根据前面传过的key来筛选自己想要的关键词的消息

根据 groupid的不同，可以对同一个主题的数据进行不同的处理，入库，统计，供数据分析等

爬取数据的时候可以多线程（生产者）

接收数据的时候也可以多线程（消费者）



![img](%E5%9B%BE%E7%89%87/04d5a3ecd021e9a6ee0037cf23cf70fa1a004b2f.png)

