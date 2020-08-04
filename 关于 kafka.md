### 关于 kafka

信息消费 https://www.kingname.info/2020/03/23/how-kafka-consume/



为什么学习 kafka https://www.kingname.info/2019/12/14/use-kakfa-in-spider/



使用python读写kafka https://www.kingname.info/2020/03/23/operate-kafka-by-python/



win10安装kafkahttps://blog.csdn.net/github_38482082/article/details/82112641

需要注意，路径一定不要太长，我直接放在 c盘下 C:\kafka_2.12-2.5.0

路径太长在启动服务的时候会报错，亲测

![image-20200804154857446](%E5%9B%BE%E7%89%87/image-20200804154857446.png)

出现 binding to port 则表示 zookeeper启动成功



![image-20200804154959795](%E5%9B%BE%E7%89%87/image-20200804154959795.png)

但是测试中文为什么无法被消费者接收到，待解答



 WARN Exception causing close of session 0x0: Unreasonable length = 1919902837 (org.apache.zookeeper.server.NIOServerCnxn)



