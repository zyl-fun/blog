### grequests模块的使用

- [ ] [github]( https://github.com/spyoungtech/grequests)
- [ ] [参考](https://blog.csdn.net/Mr_Zhen/article/details/91812974)

Create a set of unsent Requests:

创建一组未发送的请求

Send them all at the same time:

在同一时间发送它们

或者，在请求连接期间发生超时或任何其他异常时，您可以添加一个异常处理程序，该处理程序将在主线程内随请求和异常一起调用：

为了提高速度/性能，您可能还希望使用imap而不是map。imap返回一个响应生成器。这些响应的顺序与您发出的请求的顺序不对应。imap的API等同于map的API。

*自我感觉没有自己写协程+requests灵活*

