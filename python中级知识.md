## Python内存管理

Python有一个私有堆空间来保存所有的对象和数据结构

（python变量存储  https://blog.csdn.net/weixin_44038167/article/details/103412443 ）

作为开发者，我们无法访问，在解释器管理它，但是有了核心API，可以访问一些工具

Python内存管理器控制分配内存

​	**垃圾回收** --> python 不同于 c++ java (可以不用事先声明变量类型而直接对变量进行赋值)

​	对象的类型 和内存都是在运行时确定的，所以 称 Python 语言为动态类型，对变量内存地址的分配是在运行时自动判断变量类型并对变量进行赋值

内置的垃圾回收器会回收所有的未使用的内存

**分代技术 -- >**

将系统中的所有内存块根据其存活时间划分为不同的集合，每个集合为一个 代，垃圾收集的频率随着代的存活时间增大而减少

python默认定义三代对象集合，索引数越大，存活时间越长。

​	**引用计数** -->

python 采用类似windows内核对象的方式进行内存管理

每个对象，都维护着指向该对象的引用的计数，系统会自动维护这些标签，并且定时扫描，当计数为0，该对象就会被回收。

原因：
1.Python 程序在运行时，需要在内存中开辟出一块空间，用于存放运行时产生的临时变量，计算完成后，再将结果输出到永久性存储器中。
2.但是当数据量过大，或者内存空间管理不善，就很容易出现内存溢出的情况，程序可能会被操作系统终止。

3.而对于服务器这种用于永不中断的系统来说，内存管理就显得更为重要了，不然很容易引发内存泄漏。
4.这里的内存泄漏是指程序本身没有设计好，导致程序未能释放已不再使用的内存，或者直接失去了对某段内存的控制，造成了内存的浪费。

一个对象，会记录着自身被引用的次数

函数外：

```python
import gc
import os
import sys

import psutil

#显示当前python程序占用内存的大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used : {} MB'.format(hint, memory))

def func():
    global  a
    show_memory_info('before')
    a = [i for i in range(1000000)]
    show_memory_info('after')

func()
print('a 引用次数', sys.getrefcount(a))
del a #计数清零
gc.collect()#垃圾回收
show_memory_info('finished')
```

输出：

```
before memory used : 28.34765625 MB
after memory used : 67.24609375 MB
a 引用次数 2
finished memory used : 28.921875 MB
```

函数内，循环引用：

对象间的相互引用，导致对象不能通过引用计数器进行销毁

需要手动触发垃圾回收，挥手循环引用

```python
def func2():
    show_memory_info('initial')
    b = [i for i in range(1000000)]
    c = [i for i in range(1000000)]
    b.append(c)
    c.append(b)#引用一次
    print('b引用次数：',sys.getrefcount(b))
    show_memory_info('after b, c created')
func2()
gc.collect()#启动垃圾回收机制，存在的对象会被删除
show_memory_info('finished')
```

输出：

```
initial memory used : 28.65625 MB
b引用次数： 3
after b, c created memory used : 111.37109375 MB
finished memory used : 49.4453125 MB
```

python中的对象存储：

万物皆是对象，不存在基本数据类型，都会在内存中开辟一块空间进行存储

根据不同的类型以及内容，开辟不同的大小进行存储，返回该空间的地址给外界接受（引用），用于后续对这个对象的操作，id() 查看内存地址 10 进制 hex() 16进制

```
class Person():
    pass

p = Person()
print(p)
print(id(p))
print(hex(id(p)))
```

```
<__main__.Person object at 0x7f330da3cbe0>
139857248898016
0x7f330da3cbe0
```

对于整数和短小的字符， Python 会进行缓存，不会创建多个相同对象

这种情况下，被多次赋值，只会有多份引用

```
num1 = 2
num2 = 2
print(id(num1), id(num2))
```

```
10914400 10914400
```

容器对象（字典，列表，元组），存储的其他对象，仅仅是对其他对象的引用，并不是其他对象本身



**字符串驻留**

万物皆是对象

解释器碰到两个一样的对象会对其进行优化，先去驻留内存中查找

驻留内存 -->

不是所有的字符串会放到驻留内存中，内存可能会爆炸

长度 0 或者 1 字符串

只包含字母， 数字 下划线

必须是编译时的常量字符串





## 深拷贝和浅拷贝

 https://blog.csdn.net/weixin_44038167/article/details/103690356 

```
import copy
#数据储存在堆区， a, b 存储的为地址， 在栈区,指向同一个堆区
a = [1,2,[2,3]]
b = a
a.append(5)
print(b)
#浅拷贝，只记录当前已经存在的 堆区数据可以一直记录，静态区则不可以
c = copy.copy(a)
print(c)
a.append(7)
a[2].append(6)
print(c)
#深拷贝 全部都拷贝过来  堆区 静态区 都 拷贝
d = copy.deepcopy(a)

print(d)
```

```
[1, 2, [2, 3], 5] 
[1, 2, [2, 3], 5]
[1, 2, [2, 3, 6], 5]
[1, 2, [2, 3, 6], 5, 7]
```

a 和 b 都是储存 堆区的地址，浅拷贝不能拷贝静态存储区数据，深拷贝可以

对象的赋值就是简单的引用

深拷贝就是把一个对象拷贝到另一个对象中，拷贝完成，两者之间没有任何关系

浅拷贝把一个对象的引用拷贝到另一个对象，拷贝完毕，也会对另一个对象有影响

切片操作是浅拷贝

## 可变类型和不可变类型

**<u>列表和元组之间的区别</u>：**

列表可变，元组不可变数据类型（大小是固定的），决定了两者提供的方法，应用场景，性能上有很大的区别

tuple用于存储异构数据，当做没有字段名的记录来用，例如记录人的 身高 体重 年龄

```
person = ('zyl',23, 180, 65)
```

列表用于存储同构数据，即具有相同意义的数据

tuple无法指定字段名，所以引申 namedtuple 可以指定字段名， 当做轻量级的类来使用

 https://blog.csdn.net/weixin_44038167/article/details/103938997 



**<u>列表和字典的区别</u>：**

列表为序列，可以理解为数据结构中的数组，字典可以理解为数据结构中的 hashmap

都可以作为集合来存储数据

从差异特征上来看：

- list有序，dict无序
- list索引访问，dict使用键来访问
- list随着元素数量的增长要想查找元素的时间复杂度为O(n), dict 的时间复杂度不随着数量的增长而变化，为O（1）
- dict 占用内存比list 稍大

特征决定了用途：

list 可以作为队列，堆栈使用， dict 一般作为聚合统计，或者快速使用特征访问等



**可变与不可变**

 https://blog.csdn.net/weixin_44038167/article/details/103718484 

可变与不可变，是指内存中内容是否可被改变

如果为不可变类型，在对象本身操作的时候，必须在内存中新申请一块区域，因为老区域不可变

为可变类型，不需要再申请内存，只需要在此对象后面连续申请（+、-）即可，地址保持不变，但是其所在区域会变长或变短



**列表底层实现**

list ,很容易和 C++ Java 标准库中常见的链表混淆

在 CPython（C 语言实现的 python ，原汁原味的 python） 中 ，列表被实现为长度可变的数组

python 中的列表 是由对其他对象的引用组成的连续数组，指向这个数组的指针及其长度被保存在一个列表头结构中。

每次添加或者删除元素，由引用组成的数组需要重新分配大小，但是 python 在创建这些数组采用了指数过分配，所以并不是每次操作都需要改变数组的大小，也正因为这样，添加或取出元素的平摊复杂度较低

但是，在普通链表上代价很小的操作在 python 中计算复杂度却相对过高

list.insert list.delete 复杂度为O(N)



**列表推导**

https://blog.csdn.net/weixin_44038167/article/details/103343525

https://blog.csdn.net/weixin_44038167/article/details/103017171

https://blog.csdn.net/weixin_44038167/article/details/102689972

使用内置函数方便的获取索引

```
for i ,index in enumerate([1,2,3,4,68,22]):
    print(i, index)
```

```
0 1
1 2
2 3
3 4
4 68
5 22
```



**字典底层实现**

dict 将一组唯一的键映射到相应的值

在遍历字典元素时，字典里的 keys() values() items() ,返回值不再是列表，而是视图对象

CPython使用伪随机探测的散列表作为字典的底层数据结构，所以，只有可哈希的对象才能作为字典的键

*什么是可哈希的？*  https://www.cnblogs.com/sea-stream/p/10573034.html 

字典的三个基本操作，添加获取删除 的平均时间复杂度为 O(1)，但是平摊最坏情况复杂度要高得多O(N)

在复制和遍历字典的操作中，最坏的复杂度n是字典曾经达到最大元素数目，而不是当前的元素数目。简短地说，若一个字典的曾经元素个数很多，后来又大大地减少了，那么遍历这个字典可能会花费很长的时间，在某些情况下，如果需要频繁地遍历某个字典，那么最好创建一个新的字典对象，而不是仅在旧的字典中删除元素

*字典的缺点和替代方案*

字典的常见陷阱，不会按照键的添加顺序来保存元素的顺序，在某些情况下，字典的键是连续的，对应的值也是连续的

如果需要保存添加的顺序，使用 OrderDict有序字典  https://blog.csdn.net/weixin_44038167/article/details/103605919 



**集合**

集合是鲁棒性很好的数据结构

*什么是鲁棒性*  [https://baike.baidu.com/item/%E9%B2%81%E6%A3%92%E6%80%A7/832302?fr=aladdin](https://baike.baidu.com/item/鲁棒性/832302?fr=aladdin) 

当元素的重要性不如元素的唯一性，和测试元素是否包含在集合中的效率时，使用这种数据结构及其有用

 https://blog.csdn.net/weixin_44038167/article/details/103243026 

python 内置集合类型有两种

- set()可变的 无序的 有限的集合，元素唯一，
- fronzenset() 不可变的，可哈希的，无序的集合，其中的元素是唯一的，不可变的哈希对象

CPython 中的集合和字典非常相似，集合被实现为带有空值的字典，只有键才是实际的集合元素，集合还利用这种没有值得映射做了其他的优化

所以可以快速向集合中添加元素，删除元素，检查元素是否存在



## Python2与Python3的区别



## 断言



## 进程，线程，协程

 https://blog.csdn.net/weixin_44038167/article/details/102679159 

进程，是执行中的计算机程序，，每段代码在执行的时候，本身就是一个进程

进程的生命周期，就绪，运行，中断，僵死，结束（不同的操作系统不一样）

运行中每个进程都拥有自己的地址空间，内存，数据栈及其他资源

进程可以通过派生新的进程来执行其它任务，不过每个进程还是拥有自己独立的内存和数据栈等

进程之间的资源不能共享，需要进程间通信，来发送数据，接收消息等

多进程称为并行

进程间的通信： 进程队列 queue 管道 pipe

```python
import multiprocessing
import os
import time
#进程间无法共享数据,子进程引入全局变量会复制一份
num = 10
def work():
    print('开始子进程，id{}'.format(os.getppid()))
    global num
    num += 10
    print(num)
    print('结束子进程')

if __name__ == '__main__':
    print('主进程id:{}'.format(os.getpid()))#自动创建进程，主进程
    print('开始执行主进程')
    child = multiprocessing.Process(target= work)#函数后不能加括号，这样相当于在主进程执行函数，把函数的返回值传给子进程，默认函数没有返回值为None
    child.start()
    child.join()
    print(num)
    print('主进程结束')
```

```
主进程id:63101
开始执行主进程
开始子进程，id63101
20
结束子进程
10
主进程结束
```

队列和管道只是实现了数据交互，并没有实现数据共享，一个进程去更改另一个进程的数据

进程之间应该尽量避免使用共享数据的方式

#### 进程池

开多进程是为了并发，通常有几个 cpu 核心就开几个进程，但是进程开多了会影响效率，主要体现在切换的开销，所以要引入进程池限制进程的数量

进程池内部维护一个进程序列，当使用时，则去进程池去获取一个进程，如果进程池序列中没有可供使用的进程，那么进程就会等待，直到进程池中有可用进程为止



#### 线程

线程是在进程中执行的代码

一个进程可以运行多个线程，这些线程之间共享主进程内申请的操作系统的资源

一个进程中启动多个线程的时候，每个线程按照顺序执行，现在的操作系统中，也支持线程抢占，也就是说其他等待运行的线程，可以通过优先级，信号等方式，将运行的线程挂起，自己先运行

使用：

用户编写多个包含线程的程序（每个程序本身都是一个进程）

操作系统“程序切换”进入当前进程

当前进程包含了线程，则启动线程

多个线程，则按照顺序执行，除非抢占

特性：

线程，必须在一个存在的进程中启动运行

线程使用进程获得的系统资源，不会像进程那样需要申请CPU等资源

线程无法给予平均执行时间，它可以被其它线程抢占，而进程按照操作系统的设定分配时间

每个进程中，都可以启动多个线程

说明：
多线程，称为并发执行

#### 线程池

系统启动一个新线程的成本是比较高的，因为它涉及与操作系统的交互。在这种情形下，使用线程池可以很好地提升性能，尤其是当程序需要创建大量生存期很短的线程时，更应该考虑使用线程池



线程池在系统启动时即创建大量空闲的线程，程序只要将一个函数提交给线程池，线程池就会启动一个空闲的线程来执行它，当函数执行结束后，该线程并不会死亡，而是再次返回到线程池中变为空闲状态，等待执行下一个函数



使用线程池可以有效地控制系统中并发线程的数量，当系统中包含有大量并发线程时，会导致系统性能急剧下降。还可能导致解释器崩溃。而线程池的最大线程数参数可以控制系统中并发线程的数量不超过此数



#### 多线程通信

##### 共享变量

创建全局变量，多个线程共用一个全局变量，方便简单。但是坏处就是共享变量容易出现数据竞争，不是线程安全的，解决方法就是使用互斥锁

##### 变量共享引申出线程同步问题

多个线程共同对某个数据修改时，可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。

Thread对象的 LOCK RLOCK 可以实现简单的线程同步，这两个对象都有 acquire release 方法

对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire release 方法之间

##### 队列

线程间使用队列进行通信，因为队列的所有方法都是线程安全的，所以不会出现线程间竞争资源的情况

Queue.Queue 是进程内非堵塞队列



#### 进程和线程的区别

一个进程的各个线程与主进程共享相同的资源，与进程间互相独立相比，线程之间信息共享和通信更加容易，都在进程中，并且共享内存

线程并发执行，这种并发和数据共享机制，使多任务之间的协作成为可能

进程一般并行执行，这种并行使得程序能同时在多个 CPU 运行

区别于多个线程只能在进程申请到的“时间片” 内运行 （一个 CPU 内的进程，启动了多个线程，线程调度共享这个进程的可执行时间片），进程可以真正实现程序的 同时 运行 （多个 cpu 同时运行）

常用场景：



在 python 中编写并发程序的经验  https://blog.csdn.net/youanyyou/article/details/78990156 

计算密集任务使用多进程

IO密集型（网络通讯）任务使用多线程，少用多进程，因为 IO操作需要独占资源

如：网络通讯（微观每次只有一个人说话，宏观上看起来像同时聊天），每次只有一个人在说话

文件读写 同时只能有一个程序在操作（两个程序同时给同一个文件写入，文件到底写入输入的哪个）

都需要控制资源每次只能有 一个程序在使用，在多线程，由主进程 申请 IO 资源，多个线程逐个执行，哪怕抢占，也是逐个运行，感觉上 “多线程” 并发执行了



如果是多进程，除非一个进程结束，否则另一个完全不能用， 这样多进程就浪费资源了

#### 协程

 https://blog.csdn.net/weixin_44038167/article/details/102695770 

称为 微线程 Coroutine 



作用：

在 执行函数 A 时，可以随时中断，去执行 B函数，然后中断 去执行 A 函数 ，自由切换。这个过程并不是函数调用，看起来像 多线程 ，然而 协程 只有一个 线程执行



协程 是 程序主动控制切换， 没有线程切换的开销，执行效率极高，对于 IO 密集任务非常适用，若是 CPU 密集任务， 多进程 + 协程

协程间是协同调度的，在并发量数万以上时，协程性能远远高于线程



常用库 greenlet gevent



协程优点： 切换开销小，程序级别的切换，操作系统感知不到，更加轻量级

单线程就可以实现并发的效果，最大限度利用 cpu



协程缺点：

协程本质为单线程，无法利用多核，一个程序开多个进程，每个进程开多个线程，每个线程内开启协程

协程指的为单个线程，一旦协程堵塞，将会堵塞整个线程

## Python中的协程

一个协程是一个函数/子程序（函数和子程序是指一个东西）这个函数可以暂停执行，把执行权让给YieldInstruction ,等 YieldInstruct 执行完成，这个函数可以继续执行，这个函数可以多次暂停和继续

协程可以在卡住的时候干其他事情

```python
import asyncio
async def long_task():
    print('long task started')
    await asyncio.sleep(1)
    print('long task finished')
f1 = long_task()
loop = asyncio.get_event_loop()
loop.run_until_complete(f1)
print('end')
```

```
long task started
long task finished
end
```

```python
import asyncio

async def hello():
    print('hello')
    await asyncio.sleep(1)
    print('你好')
async def world():
    print('world')
    await asyncio.sleep(1)
    print('世界')
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(hello()),
        asyncio.ensure_future(world())
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    print('完成')
```

```
hello
world
你好
世界
完成
```

协程有两种定义方法:

生成器 / async

底层实现都是生成器，特征都是可以暂停执行和恢复执行

#### 协程异常处理

使用协程一定增加很多异常，百密一疏，总会有意想不到的事情发生，为了不让程序总体崩溃应该使用协程的额外异常处理方法，会执行绑定的回调函数

#### greenlet框架实现协程（封装yield基础库）

思想：生成器函数或者协程函数中的 yield 语句挂起函数的执行，直到稍后使用 next() 或 send() 操作进行恢复为止。 可以使用一个调度器循环在一组生成器之间协作多个任务

greenlet 是 python 中实现我们所谓的 coroutine(协程) 的基础库

#### 基于  greenlet 框架的高级库 gevent

是第三方库，通过 greenlet 实现协程

思想：

当 greenlet 遇到 一个 IO ，例如访问网络，就自动切换到其他的 greenlet ,等到 IO 操作完成，再在适当的时候切回来继续执行。

IO 操作非常耗时，经常让程序处于等待状态，有了 gevent 为我们自动切换协程，就保证总有 greenlet 在运行，而不是在等待 IO 

## 原生协程

协程有自己的 寄存器上下文 和 栈，协程 调度切换，将上下文和栈保存，在调度回来的时候，恢复先前保存的寄存器上下文和栈。协程能够保存上一次调用时的状态，即所有局部状态的一个特定组合

寄存器  [https://baike.baidu.com/item/%E5%AF%84%E5%AD%98%E5%99%A8/187682?fr=aladdin](https://baike.baidu.com/item/寄存器/187682?fr=aladdin) 

async函数可以看作为多个异步操作，包装为一个 Promise 对象， await命令是内部 then 命令的语法糖

*什么叫做寄存器上下文* https://blog.csdn.net/missalucard/article/details/5064683 

```python
import asyncio
import time


def job(t):
    time.sleep(t)
    print('用了%s' % t)
def main():
    [job(t) for t in range(1,3)]
start = time.time()
main()
print(time.time()-start)

async def job(t): #将函数定义为协程
    await  asyncio.sleep(t) #切换其他任务
    print('用了 %s' % t)
async def main(loop):
    tasks = [loop.create_task(job(t)) for t in range(1,3)] #创建任务，不立即执行
    await asyncio.wait(tasks) #执行并等待所有任务完成
start = time.time()
loop = asyncio.get_event_loop() #建立 loop
loop.run_until_complete(main(loop)) #执行 loop
loop.close() #关闭 loop
print(time.time()-start)
```

```
用了1
用了2
3.0036447048187256
用了 1
用了 2
2.002680540084839
```

## GIL全局解释器锁

#### GIL是什么？

全称 Global Interpreter Lock ,限制多线程同时执行，保证同一时间只有一个线程在执行。

GIL 并不是 python 的特性，是在实现 python解释器（CPython）所引入的概念。

python 和 python解释器 为两个概念，不可混为一谈。

GIL 只存在于使用 C语言编写的解释器 CPython 中

若不用 python 官方推荐的CPython 解释器，而使用其他语言编写的解释器（JPython 运行在 java上的解释器，直接把python代码编译成 java 字节码执行），就不会有GIL问题，但是 CPython是大部分环境下默认的Python执行环境。很多人概念里CPython 就是Python ，想当然的把 GIL 归结为 Python语言的缺陷。

GIL 并不是 Python的特性， Python完全可以不依赖 GIL

*什么是 java字节码？* https://blog.csdn.net/q5706503/article/details/84204747 

#### GIL的作用

为了更有效的利用多核处理器的性能，就出现了多线程的编程方式，但随之带来的就是线程间数据的一致性和状态同步的完整性。

python为了利用多核，开始支持多线程，但是线程是非独立的，所以同一进程里线程是数据共享，当各个线程访问数据资源时会出现竞争状态，即数据可能被多个线程同时占用，造成数据混乱，这里的线程就是不安全的，而解决多线程之间的数据完整性和状态同步的最简单方式就是加锁。

GIL能限制多线程同时执行，保证同一时间内只有一个线程在执行

#### GIL影响

GIL是全局排他锁，全局锁的存在对多线程的效率有不小的影响，甚至等于Python是单个线程的程序

#### 如何避免GIL带来的影响

##### 方法一：

进程 + 协程  代替 多线程的方式在多进程中，每个进程都是独立存在，所以每个进程内的线程都拥有独立的 GIL 锁，互不影响，正是这样，进程之间是独立的，通信就需要通过队列的方式来实现

##### 方法二：

更换解释器

JPython IronPython 这样的解释器由于实现语言的特性，不需要 GIL 的帮忙，然而由于用了Java / C# 用于解释器实现，也失去了利用社区众多 C语言模块有用特性的机会，所以这些解释器也因此一直比较小众

#### 其他解释器

当我们从Python官方网站下载并安装好 Python2.7后，直接获得官方解释器：CPython

c语言开发，所以叫 CPython,在命令行下运行python 就是启动CPython解释器

IPython 是基于 CPython 之上的一个交互式解释器，只是在交互方式上有所增强，但是执行 Python代码的功能和 CPython 是完全一样的。好比很多国内浏览器虽然外观上不同，但是内核都是调用了 IE



CPython 用  >>> 作为提示符， IPython In[序号]: 作为提示符

PyPy解释器，目标是执行速度，采用 JIT技术，对 Python代码进行动态编译（并不是解释），所以可以显著提高代码的执行速度

绝大部分 python代码都额可以在 PyPy下运行，它和 CPython 有一些不同，这就导致相同的 Python代码在两种解释器下执行可能会有不同的结果，

JPython 是运行在Java平台上的 Python解释器，可以直接把 Python 代码编译成 Java 字节码执行

IronPython 是运行在微软.net平台上的 Python解释器，可以直接把 Python 代码编译成 .Net的字节码

## 生成器和迭代器

#### 迭代的概念

上一次输出的结果为下一次输入的初始值，重复的过程称为迭代，每次重复即一次迭代，每次迭代的结果为下一次迭代的初始值

#### 可迭代的对象

内置 iter 方法，list,dict,set都是可迭代对象

可迭代对象就是可迭代的对象，可以从这个对象拿到迭代器，python iter 可以帮我们完成这个事情

iterable -> iterator

#### 迭代器

##### 为什么要有迭代器

对于没有索引的数据类型，必须提供一种不依赖索引迭代方式 

集合，字典不支持索引访问

##### 迭代器的定义

可迭代对象执行 iter方法，得到的结果就是迭代器，迭代器对象有 next 方法

它是一个带状态的对象，能在被调用 next() 方法的时候返回容器里的下一个值，任何实现了 iter 和 next 方法的对象都是迭代器， iter 返回迭代器自身， next  返回容器里的下一个值， 若 容器里没有元素，则抛出 StopIteration 异常

##### 生成器的定义

它是一个特殊的迭代器，其实现更加的简单优雅， yield是生成器实现 next()  方法的关键。它作为生成器执行的暂停恢复点，可以对 yield 表达式进行赋值，也可以将 yield 表达式的值返回

yield是一个语法糖，内部实现支持了 迭代器协议，同时 其内部是一个状态机，维护着挂起和继续的状态

生成器一般是使用函数来实现的

```python
def generator_function():
    for i in range(10):
        yield i
for item in generator_function():
    print(item)
```

利用生成器实现斐波那契数列

```
def fib(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b
for x in fib(44):
    print(x)
```

```python
strs = 'hhxhxhxxhxhxh'
str1 = iter(strs)
print(next(str1))
print(next(str1))
print(next(str1))
print(next(str1))
print(next(str1))
```

```
h
h
x
h
x
```



##### yield功能

相当于为函数封装好 iter next ,return只能返回一次值，函数便终止，而 yield能返回多个值，每次返回都会将函数暂停，下一次next 会从上一次暂停的位置继续执行

##### 为什么说生成器是一种迭代器

Python判断一个对象是否为迭代器的标准就是看这个对象是否遵守迭代器协议，判断一个对象是否遵守迭代器协议体现在下面两个方面

iter 和 next 方法

iter必须返回的是对象的本身

生成器恰好满足这两个条件。

list是个可迭代对象，当我们使用 for ... in ,python会给我们生成一个迭代器对象，迭代器是一个数据流，它可以产生数据，我们可以在里面取，而不需要 像 C 语言代码维护 (数组 index),python已经通过迭代器帮我们解决了这个问题

## 类方法和静态方法

普通实例方法，第一个参数是 self ，它表示一个具体的实例本身

staticmethod ,可以无视 self

classmethod ，第一个参数是 cls,表示类本身

@classmethod 修饰符对应的函数不需要实例化，不需要 self 参数

```python
class Foo():
    def instance_method(self):
        print('实例方法只能被实例对象调用')
    @staticmethod
    def static_method():
        print('我是静态方法')
    @classmethod
    def class_method(cls):
        print('我是类方法')
foo = Foo()
foo.instance_method()
foo.static_method()
foo.class_method()
print('+++++++++')
Foo.static_method()
Foo.class_method()
```

```python
class C():
    @staticmethod
    def f():
        print('444')
C.f()
c = C()
c.f()
```

输出：

```
444
444
```

```python
class A():
    num = '类属性'
    def fun1(self):
        print('fun1')
        print(self)
    @classmethod
    def fun2(cls):
        print('fun2')
        print(cls)
        print(cls.num)
        cls().fun1()
    def func3():
        print('func3')
        print(A.num)
A.func3()
A.fun2()
```

```
func3
类属性
fun2
<class '__main__.A'>
类属性
fun1
<__main__.A object at 0x7fe7dfa7a898>
```

## 上下文管理（with）

with是一种上下文管理协议，目的在于从流程图中 把 try except finally关键字和资源分配释放相关代码统一去掉，简化 try ...except...finally的处理流程。

with通过 enter 方法初始化，然后在 exit 中做善后以及处理异常。

使用 with处理的对象必须有 enter() 和 exit() 这两个方法

enter()方法在语句体(with 语句包裹起来的代码)，执行之前进入运行，exit()方法在语句执行完毕退出后运行。with语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的 “清理”操作，释放资源，比如文件使用后自动关闭,线程中锁的自动获取和释放

with使用场景，如果某项工作完成后需要释放资源或者其他清理工作，如文件操作，便可以使用 with ,不用自己手动关闭文件句柄，而且还能很好地管理上下文异常

```python
with open('test33.py') as fp:
    for line in fp:
        print(line)
```

工作原理：

with后面的语句被求值后，该语句返回的对象的 enter()方法被调用，这个方法将返回的值赋给 as 后面的变量，当 with 包围 的语句快全部被执行完毕后，自动调用 对象的 exit() 方法。

with 处理异常会更方便，省去 try except finally复杂的流程，用到的便是对象的 exit （）方法：

exit(exc_type, exc_value,exc_trackback)后面的三个参数是固定的，用来接收 with 执行过程中的异常类型，名称和详细信息

```python
class Echo:
    def output(self):
        print('hello')
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        if exc_type == ValueError:
            return True
        else:
            return False

with Echo() as e:
    e.output()
    print('do something inside')


print('-------------')
with Echo() as e:
    raise ValueError('Value Error')

print('-------------')
with Echo() as e:
    raise Exception("can't not detect")
```

```
Traceback (most recent call last):
  File "/home/zhang/PycharmProjects/flask_three/myapp/with_test.py", line 26, in <module>
    raise Exception("can't not detect")
Exception: can't not detect
enter
hello
do something inside
exit
-------------
enter
exit
-------------
enter
exit
```

**contextlib**

with语句的加强版本，通过生成器实现的

其中的 contextmanager作为装饰器来提供一种针对函数级别的上下文管理机制

```
from contextlib import contextmanager

@contextmanager
def make_context():
    print('enter')
    try:
        yield {}
    except RuntimeError as e :
        print(e)
    finally:
        print("exit")
with make_context() as value:
    print(value)
```

```
enter
{}
exit
```

contextlib 支持嵌套， closing 帮助自动执行定义好的close函数

```
from contextlib import contextmanager
from contextlib import closing

@contextmanager
def make_context(name):
    print('enter',name)
    yield name
    print('exit', name)


with make_context('A') as a, make_context('B') as b:
    print(a)
    print(b)


class Door():
    def open(self):
        print('Door is opened')
    def close(self):
        print('Door is closed')

with closing(Door()) as door:
    door.open()
```

```
enter A
enter B
A
B
exit B
exit A
Door is opened
Door is closed
```



## 高阶函数

#### map

接受两个参数，一个为函数，接收一个参数，一个是序列，将传入的函数依次作用到每个元素，并返回一个新的 Iterator



字符串基本知识点：

 [http://39.107.46.92/jqxx/6%20%E5%AD%97%E7%AC%A6%E4%B8%B2%E3%80%81%E5%85%83%E7%BB%84.pdf](http://39.107.46.92/jqxx/6 字符串、元组.pdf) 

```python
def f(s):
    return s.title()
list1 = map(f,['python','JaVA','PHP'])
print(list(list1))
```

map函数返回的是迭代器

#### reduce

把传入的函数作用到序列上，传入的函数需要接受两个参数，传入的函数计算结果继续和序列的下一个元素做累计计算

```python
from functools import reduce
def f(x,y):
    return x + y
print(reduce(f,['abb','ccc','d','e']))
```

#### filter

接受一个函数和一个序列，将函数作用到序列中的每一个元素，如果传入的函数返回 true,保留元素，否则丢弃

最终返回迭代器

```
def  f(s):
    return s.isalpha()
l = filter(f,['acv','aaa','12a','222'])
print(list(l))
```

#### sorted

 https://blog.csdn.net/weixin_44038167/article/details/102806795 

## 设计模式

Python设计模式，为了解决面向对象系统中重要和重复的设计封装在一起的一种代码实现框架，可以使得代码更加易于扩展和调用

四大要素：

模式名称，问题，解决方案，效果



六大原则：

1. 开闭原则，一个软件实体，类/模块/函数 应该对扩展开放，对修改关闭，就是 软件实体应尽量在不修改原有代码的情况下进行扩展
2. 里氏替换原则：所有引用 父类的方法必须能透明的使用其子类的对象
3. 依赖倒置原则：高层模块不应该依赖底层模块，二者都应该依赖其抽象，抽象不应该依赖于细节，细节应该依赖抽象，就是要针对接口编程而不是针对实现编程
4. 接口隔离原则：使用多个专门的接口，而不是使用单一的总接口，客户端不应该依赖那些并不需要的接口
5. 迪米特法则：一个软件实体应该尽可能的少与其他实体相互作用
6. 单一职责原则：不要存在多个导致类变更的原因，一个类只负责一个职责



##### 接口

一种特殊的类，声明了若干方法，要求继承该接口的类必须实现这种方法

作用：限制继承接口的类的方法的名称及调用方式，隐藏了类的内部实现

```
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self,money):
        pass
class AiliPay(Payment):
    def pay(self,money):
        print('使用支付宝支付%s' %money)

class ApplePay(Payment):
    def pay(self,money):
        print('使用苹果支付 %s' % money)
```

ABC Abstract Base Class 抽象基类

定义了基本类的和最基本的抽象方法，可以为子类定义共有 API，不需要具体实现

 https://www.cnblogs.com/anzhangjun/p/9780463.html 

##### 单例模式

 https://blog.csdn.net/weixin_44038167/article/details/102628073 

保证一个类只有一个实例，并提供一个访问它的全局访问点

适用场景：

当一个类只能有一个实例，而客户可以从一个众所周知的访问点访问它时

优点：

对唯一实例的受控访问，相当于全局变量，又可以防止此变量被篡改

```
class Singleton():
    #若该类已经有了一个实例则直接返回，否则创建一个全局唯一实例
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self, name):
        if name:
            self.name = name


a = MyClass('a')
print(a)
print(a.name)

b = MyClass('b')
print(b)
print(b.name)

print(a)
print(a.name)
```

```
<__main__.MyClass object at 0x7effca377710>
a
<__main__.MyClass object at 0x7effca377710>
b
<__main__.MyClass object at 0x7effca377710>
b
```

##### 工厂模式（celery）

不直接向客户暴露对象创建的实现细节，通过一个工厂类来负责创建产品类的实例

角色：

工厂角色，抽象产品角色，具体产品角色

优点：

隐藏对象创建代码的细节，客户端不需要修改代码

缺点：

违反了单一职责原则，将创建逻辑集中到一个工厂里面，当要添加新产品时，违背了开闭原则

```
from abc import ABCMeta, abstractmethod


class PayMent(metaclass=ABCMeta):
    #抽象产品角色
    @abstractmethod
    def pay(self,money):
        pass

class AliPay(PayMent):
    #具体产品角色
    def __init__(self,enable_yuebao = False):
        self.enable_yuebao = enable_yuebao
    def pay(self,money):
        if self.enable_yuebao:
            print('使用余额宝支付%s元' % money)
        else:
            print('使用支付宝支付%s元'% money)
class ApplePay(PayMent):
    def pay(self,money):
        print('使用苹果支付%s元' % money)
class PaymentFactory():
    #工厂角色
    def create_payment(self,method):
        if method == 'alipay':
            return AliPay()
        elif method == 'yuebao':
            return AliPay(True)
        elif method == 'applepay':
            return ApplePay()
        else:
            return NameError
p = PaymentFactory()
f = p.create_payment('yuebao')
f.pay(100000000)
```

```
使用余额宝支付100000000元
```

##### 观察者模式

定义：

对象间的一种一对多的依赖关系，一个对象状态发生改变时，所有依赖它的对象都会得到通知并被自动更新，观察者模式又被称为  发布订阅模式

角色：

抽象主题，具体主题（发布者），抽象观察者，具体观察者（订阅者）

场景：

一个抽象模型有两个方面，其中一个依赖另一个，将两者封装在独立的对象中以使它们各自独立的改变和复用

当一个对象的改变需要同时改变其它对象，而又不知道具体有多少对象以待改变

当一个对象必须通知其他对象，而又不知道其他对象是谁，这些对象之间是解耦的



优点：

目标和观察者之间耦合最小，支持广播通信

缺点：

多个观察者互不知道对方的存在，因此一个观察者对主题的修改可能造成错误的更新

```
from abc import ABCMeta, abstractmethod

#抽象主题

class Oberserver(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

#具体主题
class Notice:
    def __init__(self):
        self.observers = []
    def attach(self,obs):
        self.observers.append(obs)
    def detach(self,obs):
        self.observers.remove(obs)
    def notify(self):
        for obj in self.observers:
            obj.update(self)

# 抽象观察者
class ManagerNotice(Notice):
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info
    @company_info.setter
    def company_info(self,info):
        self.__company_info = info
        self.notify()
#具体观察者
class Manager(Oberserver):
    def __init__(self):
        self.company_info = None
    def update(self,noti):
        self.company_info = noti.company_info

#消息订阅 发送
notice = ManagerNotice()
alex = Manager()
tony = Manager()

notice.attach(alex)
notice.attach(tony)
notice.company_info = '公司运行良好'
print(alex.company_info)
print(tony.company_info)


notice.company_info = '公司将要上市'
print(alex.company_info)
print(tony.company_info)

notice.detach(tony)
notice.company_info = '公司要破产了'
print(alex.company_info)
print(tony.company_info)
```

```
公司运行良好
公司运行良好
公司将要上市
公司将要上市
公司要破产了
公司将要上市
```

## 单元测试

传统测试为 运行程序 查看结果，前后端服务进行联调

单元测试为 只测试当前单元的程序或者代码，当前模块的 代码

单元测试假设所有的内部或者外部的依赖是稳定的，已经在别处进行测试过，使用 mock可以对外部依赖组件实现进行模拟并且替换掉

mock可以帮我们解决测试依赖的一个模块

```python
import unittest
def add_and_multiply(x,y):
    adddtion = x + y
    mutiple = multiply(x,y)
    return (adddtion, mutiple)
def multiply(x,y):
    return x * y
class MyTestCase(unittest.TestCase):

    def test_add_and_multiply(self):
        x = 3
        y = 5
        addition, multiple = add_and_multiply(x,y)
        self.assertEqual(8,addition)
        self.assertEqual(15,multiple)
if __name__ == '__main__':
    unittest.main()
```

python本质上并不是做计算任务的，它是一门胶水语言，用来写业务逻辑的，不是用来写cpu密集算法的

复杂的解释器都是用 c++ 这种硬核语言来编写

程序员除了和 PM 撕逼， 在写 CRUD

瓶颈在 IO 问题上

多进程，多线程，AsyncIO Gevent

## 测试 python cpu瓶颈

需要 cProfile 模块

是一种确定性分析器，只测量CPU时间，并不关心内存消耗和其它与内存关联的信息



## python 魔术方法

 [http://39.107.46.92/jqxx/python%20%E9%AD%94%E6%9C%AF%E6%96%B9%E6%B3%95.pdf](http://39.107.46.92/jqxx/python 魔术方法.pdf) 



例子：

```
class FileObject:
    def __init__(self,filepath='/home/zhang/PycharmProjects/flask_three/cookbook',filename='test33.py'):
        self.file = open(join(filepath,filename),'r+')

    def __del__(self):
        self.file.close()
        del self.file
```

## 微服务和RPC框架

https://v3u.cn/book/p16.html

#### RPC框架

Remote Produce Call

RPC 是一个软件结构概念，是构建分布式应用的理论基础

#### Thrift

实现了 C/S 模式

最初由 facebook 开发

Apache Thrift 是一款跨语言的服务框架，传输数据采用二进制，相对于 XML JSON 体积更小。对于高并发，大数据量和多语言的环境更有优势

Thrift是一种接口描述语言和二进制通讯协议，被用来定义和创建跨语言的服务

按照 Thrift定义的语法编写 .thrift,用其命令生成各种语言的代码，调用这些代码可以完成客户端和服务端的通信，不需要自己写网络请求，数据解析等接口



例子：

 https://gitee.com/super__man/qqq/tree/master/flask_three/mythrift 

需要注意的是，在server 填写的为私有IP，client填写的为公网IP

## 算法

#### 八大排序

##### 插入排序

将一个数据插入到已经排好序的有序数据中，从而得到一个新的，个数加一的有序数据，适用于少量数据的排序。

将第一个作为已经排好序的，然后每次从后取出插入到前面并排序



```python
def insert_sort(ilist):
    for i in range(len(ilist)):
        for j in range(i):
            #如果索引为1小于索引为0，就在索引为0插入较小的，将原来小的位置元素弹出
            if ilist[i] < ilist[j]:
                ilist.insert(j,ilist.pop(i))
                break
    return ilist
ilist = [1,2,3,22,4,5,6,7,111,2,3,888]
print(insert_sort(ilist))
```

```
[1, 2, 2, 3, 3, 4, 5, 6, 7, 22, 111, 888]
```

##### 冒泡排序

要重复走访要排序的数列，一次比较两个元素，若顺序错误则交换

重复进行直到没有需要交换为止，表明该数列已经排序完成

```
def bubble_sort(blist):
    count = len(blist)
    for i in range(count):
        for j in range(i+1,count):
        	#循环往复，每一次都会找到当前最小的那个元素，把它放到最前面，从小到大排序
            if blist[i] > blist[j]:
                blist[i],blist[j] = blist[j], blist[i]
    return blist
print(bubble_sort(ilist))
```

##### 快速排序

通过一趟排序把要排序的数据分为两部分，其中一部分的所有数据都比另外一部分的所有数据小，循环使用这种方法，层层分割，递归进行，最后达到整个数据变为有序数列

```
def quick_sort(qlist):
    if qlist == []:
        return []
    else:
        qfirst = qlist[0]
        qless = quick_sort([l for l in qlist[1:] if l < qfirst])
        qmore = quick_sort([m for m in qlist[1:] if m >= qfirst])
        return qless + [qfirst] + qmore
print(quick_sort(ilist))
```



第 i 趟在待排序记录r[i] ~ r[n] 找出最小的记录，将它和r[i]交换，使有序序列不断增长



```
def select_sort(slist):
    for i in range(len(slist)):
        #认定 i 为最小，x的作用记录当前最小元素的下标
        x = i
        for j in range(i,len(slist)):
            if slist[j] < slist[i]:
                #循环挑出 j 为最小
                x = j
        slist[i], slist[x] = slist[x],slist[i]
    return slist
print(select_sort(ilist))
```

##### 归并排序

分治法，将已经有序的子序列合并，得到完全的有序序列

先使每个子序列有序，再让子序列段 有序。

将两个有序表合并为一个有序表，成为二路合并

```
def merge_sort(array):
    def merge_arr(arr_l,arr_r):
        array = []
        while len(arr_l) and len(arr_r):
            if arr_l[0] <= arr_r[0]:
                array.append(arr_l.pop(0))
            elif arr_l[0] > arr_r[0]:
                array.append(arr_r.pop(0))
        if len(arr_l) != 0:
            array += arr_l
        elif len(arr_r) != 0:
            array += arr_r
        return array

    def recursive(array):
        if len(array) == 1:
            return array
        mid = len(array) // 2
        arr_l = recursive(array[:mid])
        arr_r = recursive(array[mid:])
        return  merge_arr(arr_l,arr_r)
    return recursive(array)
print(merge_sort(ilist))
```

#### 查找算法

##### 顺序查找

又被称为线性查找，是最简单的查找方式，适用于线性表的顺序存储结构和链式存储结构

时间复杂度O(n)

从第一个元素  m 开始逐个与需要查找的元素 X 进行比较，当比较元素相同时，返回 m 下标，如果到最后都没有找到，返回 -1 

缺点：

当元素数目很多时，平均查找长度较大，效率低

优点：

对表中数据元素的存储没有要求。

对于线性表，只能进行顺序查找

```
def sequential_search(lis,key):
    length = len(lis)
    for i in range(length):
        if lis[i] == key:
            return i
    return False
```

##### 折半查找

二分查找，是一种在有序数组中查找某一特定元素的查找算法，查找过程从数组的中间元素开始查找，如果中间元素正好是要查找的元素，则查找过程结束。如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半查找，而且跟开始一样从中间元素开始比较。若某一步骤中数组为空，则代表找不到。

这种查找算法每一次比较都会使查找范围缩小一半

 时间复杂度为 O(logn) 空间复杂度：O(1) 

```
def binary_search(lis,key):  
    low = 0                  
    high = len(lis) - 1      
    time = 0                 
    while low <= high:       
        time += 1            
        mid = int((low + high) / 2 )
        if key < lis[mid]:   
            high = mid - 1   
        elif key > lis[mid]: 
            low = mid + 1    
        else:                
            print("times:%s")
            return mid       
    print('times:%s' % time) 
    return False             
print(binary_search(lis,65)) 
```

##### 插值查找

根据要查找关键字key与表中最大最小记录的关键字比较后的查找方法

计算公式：

  (key-a[low])/(a[high]-a[low])*(high-low) 

 时间复杂度o(logn)但对于表长较大而关键字分布比较均匀的查找表来说，效率较高 

基于二分查找，将查找点的选择改进为自适应选择，可以提高查找效率

  注：对于表长较大，而关键字分布又比较均匀的查找表来说，插值查找算法的平均性能比折半查找要好的多。反之，数组中如果分布非常不均匀，那么插值查找未必是很合适的选择。 

 复杂度分析 时间复杂性：如果元素均匀分布，则O（ log n）），在最坏的情况下可能需要O（n）。 空间复杂度：O（1） 

```
def binary_search(lis,key):
    low = 0
    high = len(lis) - 1
    time = 0
    while low <= high:
        time += 1
        mid = low + int((high - low) * (key - lis[low]) / (lis[high] - lis[low]))
        if key < lis[mid]:
            high = mid -1
        elif key > lis[mid]:
            low = mid + 1
        else:
            print('time:%s' % time)
            return mid
    print("time:%s" % s)
    return False

if __name__ == '__main__':
    lis = [1,2,4,22,67,555,3455]
    print(binary_search(lis,555))
```

#### 递归

调用一个函数的过程中，直接或间接调用自身这个就叫做递归，为了避免死循环，要有结束条件

```
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(4))
```

##### 汉诺塔

大一的时候就碰到过这个问题，那时候还是很好学的，回宿舍的路上都在想这个问题

```
def func(n):
	if n == 1:
		return 1
	return 2*func(n-1) + 1
```



## 数据结构

数据结构是某以种特定的布局方式存储数据的容器

这种布局方式决定了数据结构对于某些操作是高效的

而对于其他的一些操作是低效的

需要了解各种数据结构，才能在处理实际问题时选取最合适的数据结构



数据是计算机当中最关键的实体，而数据结构则可以将数据以某种组织形式存储。

则数据结构的价值不言而喻

不论你以何种方式解决问题，都需要处理数据

数据需要根据不同的场景，按照特定格式进行存储，有很多数据结构能够满足以不同格式存储数据的需求



数组/栈/队列/链表/树/字典树（一种高效的树形结构）/散列表（哈希表）

#### 数组

数组是最简单，使用最广泛的数据结构

其他数据结构都是由数组演化而来

Insert Get Delete Size

#### 栈

撤销操作遍布每一个应用

按照将最后的状态排列在先的顺寻，在内存中存储历史工作状态

后进先出 LIFO

Push在顶部插入元素

Pop返回并移除栈顶元素

isEmpty 如果栈为空返回 True

Top 返回栈顶元素，但是不移除它



##### 使用栈计算后缀表达式：

在我们日常编程，括号都是成对出现

凡是遇到括号的前半部分，把这个元素入栈，遇到后半部分对比栈顶元素是否和该元素匹配。

如果匹配，前半部分出栈，否则报错



##### 把十进制转化为其他任意进制

求余法，若转化8进制，除以8，记录余数，商继续除以8，直到商为 0，把余数倒过来写就可以

#### 队列

和栈相似，队列是另一种顺序存储元素的线性数据结构

栈和队列的最大差别在于栈书 LIFO，队列却是 FIFO

队列实现的例子，售票亭排队队伍，若有新人加入，需要到队尾去排队，总之排在前面的人会拿到票

Enqueue 尾部插入元素

Dequeue  移除队列头部元素

isEmpty 如果队列为空，则返回 True 

Top 返回队列的第一个元素



面试常见问题：

使用队列表示栈/对队列的前 k 个元素倒序/使用队列生成 1到 n 的二进制数

#### 链表

链表是另外一个重要的线性数据结构，乍一看像数组，但在内存分配，内部结构，数据插入和删除操作方面均有不同

链表就像一个节点链，其中每个节点包含着数据和指向后续节点的指针。

链表还包含一个头指针，它指向链表的第一个元素，当链表为空时，指向null或者无具体内容

链表一般用于实现 文件系统，哈希表，邻接表

链表包含以下类型：

单链表（单向）/ 双向链表（双向）

链表基本操作：

InsertAtEnd 链表尾部插入指定元素

InsertAtHead 头部插入指定元素

Delete 从链表中插入指定元素

DeleteAtHead 删除链接列表的第一个元素

Search 从链表中返回指定元素

isEmpty 如果链表为空，返回 True



面试问题

反转链表

检测链表中的循环

返回链表倒数第 N 个节点

删除链表中的重复项

#### 树

树形结构是一种层级式的数据结构，由顶点和连接它们的边组成

树类似于图，但区分树和图的重要特征是树中不存在环路

树形结构广泛应用于人工智能和复杂算法，它可以提供解决问题的有效存储机制

Root 根节点

Parent 父节点

Child 子节点

Leaf 叶子节点

Sibling 兄弟节点



树形结构的主要类型：

N 元树 平衡树 二叉树 二叉搜索树 AVL树 红黑树 2-3树

二叉树和二叉搜索树是最常用的树



面试：

求二叉树的高度

在二叉树查找第 K 个最大的值



##### 字典树 单词查找树

称为 前缀树，是一种特殊的树状数据结构，对解决字符串相关问题非常有效

提供快速检索，用于搜索字典中的单词，在搜索引擎中自动提供建议，用于 IP的路由

#### 哈希表

Hashing

一个用于唯一标识对象并将每个对象存储在一些预先计算的唯一索引（键）

对象以键值对的形式存储，这些键值对的结合被称为 字典，可以使用 键搜索每个对象。

基于哈希法有很多不同的数据结构，但最常用的数据结构是哈希表

哈希表通常使用数组实现

## 数据库相关  https://v3u.cn/book/mysql.html 

高负载高并发环境下，数据业务层，数据访问层，如果还是传统的数据结构，或者只是单单靠一台服务器负载，如此多的数据库连接操作，数据库必然崩溃，若数据库宕机，后果不堪设想

如何减少数据库的连接，采用优秀的代码框架，进行代码的优化，采用优秀的数据库缓存技术：Redis

若资金丰厚，假设 mysql 服务集群，来分担主数据库的压力

利用MySQL 主从配置，实现读写分离，减轻数据库的压力

 https://v3u.cn/a_id_85 



MySQL 主从同步原理：

从库中生成两个线程，一个 I/O，一个SQL 线程

I/O 线程去请求主库的 binlog(二进制日志)，将得到的 binlog 写到 relay log(中继日志)文件中，主库会生成 log dump 线程，用来给  I/O 线程传 binlog

SQL线程，会读取 relay log 文件中的日志，并解析成具体操作，来实现主从的操作一致，而最终数据一致。

#### binlog日志

是二进制文件，用于记录 mysql 的数据更新或者潜在更新（比如 Delete语句执行删除而实际并没有符合条件的数据）

### Redis

 http://39.107.46.92/jqxx/Redis.pdf 



本质上是一个 key - value 类型的内存数据库，很像 memcached 

整个数据库统统加载在内存当中，定期通过异步操作把数据库数据 flush 到硬盘上保存

纯内存操作，Redis性能非常出色，可以处理每秒超过 10 万次读写操作

Redis支持保存多种数据结构，此外单个 value 的最大限制是 1GB

可以用其 list 来做 FIFO双向链表，实现轻量级的高性能消息队列服务

用其 set 可以做高性能的 tag 系统

可以对存入的 key - value 设置 expire 时间，可以被当作功能加强版的 memcached来用

缺点：数据库容量受到物理内存的限制，不能作海量数据的高性能读写，Redis使用场景局限在较小的数据量的高性能操作和运算上

#### Redis好处

1. 速度快，因为数据在内存中
2. 支持丰富的数据类型 string list set sorted set hash
3. 支持事务，操作都是原子性，要么对数据的更改全都执行，要么全不执行
4. 丰富的特性，用于缓存，消息，按 key 设置过期时间，过期后自动删除

#### 为什么redis需要把所有数据放到内存中？

为了达到最快的读写速度将数据都读到内存中，通过异步的方式将数据写入磁盘，Redis拥有快速和持久化的特征。

如果设置了最大使用内存，则数据已有记录数到达到内存限值后不能继续插入新值

#### Redis单进程单线程

利用队列技术将并发访问变为串行访问，消除了传统数据库串行控制的开销

#### 单线程 Redis 为什么这么快

纯内存操作

单线程，避免了频繁的上下文切换

采用了非堵塞 I / O多路复用机制

#### Redis持久化的方式

##### 快照

把数据快照放在磁盘的二进制文件中，dump.rdb

可以自己配置持久化策略

例如数据采集中每 N 秒有超过 M次更新，就把数据写入磁盘

可以手工调用命令 SAVE / BGSAVE



Redis forks

子进程把数据写到临时 RDB文件

子进程完成写 RDB，用新文件替换老文件

使用 copy-on-write技术

##### AOF

快照模式并不健壮，当系统停止，或者五一中Redis被 kill掉，最后写入的数据就会丢失

对于要求高可靠性的应用，这方面 Redis 不是一个很好地选择

Append only 可以在配置文件打开 AOF 模式

##### 虚拟内存

当 key 很小 ，value很大，使用 VM 效果比较好，这样节省的内存比较大

当key 不小时，可以考虑将很大的 key 变成很大的 value ,比如可以把 key  value 组合成新的 value

vm-max-threads这个参数，可以设置 访问 swap 文件的线程数，设置不超过机器的核数，若 为0，那么所有 对 swap 文件的操作都是串行的，会造成较长时间的延迟，但是对数据完整性有很好的保护

##### Redis分布式锁

 Redis Setnx（**SET** if **N**ot e**X**ists） 命令在指定的 key 不存在时，为 key 设置指定的值。 

先拿 setnx 争抢锁，抢到后，用expire 给锁设置过期时间防止锁忘了释放

set指令有非常复杂的参数，可以把 setnx 和  expire 合成一条指令来用

##### redis 有一亿个 key ,其中 10w 是以某个固定的前缀开头，如何找出？

keys扫描出指定模式的列表



若redis正在使用中，使用 keys 有什么问题？

redis为单线程，keys会导致 线程堵塞，线上服务会停顿，直到指令执行完毕，服务才能恢复

使用 scan指令可无堵塞的提取出指定模式的 key 列表，但会有一定的重复率，在客户端去重就可以，整体时间会比 keys 指令长

scan命令  http://doc.redisfans.com/key/scan.html 

##### Redis 异步队列

一般使用 list结构作为 队列，rpush生产消息，lpop 消费消息，当lpop没有消息，适当 sleep 再重试

list 指令 blpop 没有消息堵塞直到消息到来



生产一次消费多次：

使用 pub/sub 主题订阅者模式，可以实现 1:N 的消息队列



pub/sub缺点：

消费者下线，生产的消息会丢失，可以使用专业的消息队列 rabbitmq :  https://blog.csdn.net/dd18709200301/article/details/79077839 



redis 延时队列

zset,拿时间戳作为 score ,消息内容作为 key调用 zadd 生产消息，消费者使用 zrangebyscore获取N秒前的数据轮询进行处理

##### 大量 key 需要设置同一时间过期，需要注意什么？

可能会出现短暂卡顿现象，在时间上加一个随机值，使得过期时间分散一些

##### Pipeline好处

缓存多条命令，依次执行，可以减少服务器和客户端之间传输次数，从而提高效率

将多次 IO 往返的时间压缩为一次，前提是pipeline执行的指令之间没有因果相关性

##### redis 同步机制

主从同步，从从同步，第一次同步，主节点做一次 bgsave（ https://www.runoob.com/redis/server-bgsave.html ）,同时将后续修改操作记录到内存 buffer,待完成后将 RDB文件全量同步到复制节点，复制节点接受完成将 rdb镜像加载到内存，加载完成后，再通知主节点将期间修改的操作记录同步到复制节点进行重放就完成了同步过程

##### redis集群，集群的原理

Redis Sentinal 着眼于 高可用，在 master 宕机会自动将 slave提升为 master,继续提供服务。

Redis Cluster 着眼于扩展性，单个 redis 内存不足，使用 cluster 进行分片存储

##### Redis并发竞争问题

主要发生在并发写竞争

redis 没有像 db 中的 sql 语句

假设某个 key = 'pirce' value值为10，想要 value + 10  操作。

正常逻辑，先把 key 为 price 的值读回来，加10，再设置回去，有一个连接没有问题，如果两个连接，还想进行这种操作，就会出现问题了



解决：

一，使用乐观锁的方式进行解决（成本低，非堵塞，性能高）

```
watch price
get price $price
$price = $price + 10
mutil
set price $price
exec
```

watch 监控该 key 值，后面的事务是有条件的执行，从 watch 的 exec 语句执行时，watch的key 对应的 value 被修改了，则事务不会执行



二，针对客户端，要对 redis 操作的时候，针对同一 key 的资源，先进行加锁



三，利用 redis setnx实现内置锁

##### redis和 memcached区别

1. 都是把数据放到内存中，都是内存数据库，memecache 可以缓存其他东西，视频，图片
2. Redis不仅支持 k/v 类型，还提供 list,set,hash等数据结构
3. Redis 虚拟内存
4. 过期策略，memcache在 set就指定，Redis通过 expire
5. 分布式，一主多从
6. 存储数据安全，memcache挂掉，数据没了，redis可以定期保存到磁盘
7. 灾备，memcache挂掉，数据不可恢复，Redis通过 aof恢复
8. Redis支持数据的备份

redis 应用于数据量较小的更性能操作和运算

memecache 用在动态系统减少数据库的负载，提升性能，做缓存（适合读多写少）

MongoDB 解决海量数据的访问效率问题



