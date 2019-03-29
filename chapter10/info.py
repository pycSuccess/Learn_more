#coding:utf-8

'''

多线程 多进程和线程池编程

1、python中的GIL

    python中一个线程对应C语言的一个线程
    GIL使得同一个时刻只有一个线程在cpu上执行字节码  无法将多个线程映射到多个cpu上  。也就是说在一个cpu中同一时刻只能运行一个线程
    虽然是全局锁但是当读取一定行数的字节码的时候就会进行释放操作 还有就是当遇到IO的时候也会进行释放

2、多线程编程--threading

    from threading import Thread

3、共享变量--Queue   这个只能是队列形式 要是dict或者其他数据结构的时候就是用共享变量

    from queue import Queue  线程安全的

    put  get   put_nowait  get_nowait    task_done   join 成对存在 在进行join时候通过task_done 就会停止下来

4、线程同步 Lock RLock

    acquire  release    获取和释放锁
    循环锁  就是一个语句的执行需要获取两把锁 这时候一个线程获取了一个就造成了死锁
    这时候就出现了RLock  这个会进行计算acquire防止出现死锁的情况
    锁机制会造成性能问题所以要适当用锁 而且在锁逻辑中尽量锁行代码

5、线程同步 condition使用以及源码分析

    条件变量，用于复杂的线程间同步
    必须使用with   wait  notify
    启动顺序很重要
    **  内部逻辑
    在调用with cond之后才能调用wait或者notify
    condition有两层锁，一把底层锁会在线程调用了wait方法时释放，上面的锁会在每次调用wait的时候分配一把
    并放入到cond的等待队列中，等待notify方法的唤醒

6、线程同步 Semaphore 使用以及源码分析

    是用于控制数量的锁
    场景： 1、文件的 读写  写一般只是用于一个线程写  读可以运行有多个
             2、爬虫

    注意的点是：获取和释放的时机   获取是为了控制   释放是进行重新赋值

7、线程池  ThreadPoolExecutor

    from concurrent import futures  (在futures里存在ThreadPoolExecutor  ProcessPoolExecutor as_completed)

    为什么要线程池：
    1.主线程中科院获取某一个线程的状态或者某一个任务的状态，以及返回值
    2.当一个线程完成的时候我们主线程能够立即知道
    3.futures可以让多线程和多进程编码接口一致

    Futrue.done判断是否完成  Futrue.result获取执行结果   Futrue.cancel 取消（只有在未开始的时候才可以）
    要看一下Future的源码  很重要

8、多线程和多进程对比

    耗cpu使用多进程编程（切换代价更大）    对于IO操作来说使用多线程编程

9、multiprocessing 多进程编程

    from multiprocessing import Process  是独立空间
    父进程已经结束了子进程还存在  孤儿进程还是僵尸进程呢？
    imap 按照可迭代列表输入
    imap_unorder  谁先完成谁先输入

10、进程间的通信  Queue  Pipe  Manager

    为什么  queue.Queue不能在进程中做通信使用  是因为机制不同找不到
    全局变量不能适用于多进程编程中 因为是彼此独立的

    multiprocessing中的queue不能用于pool进程池
    pool中的进程间通讯需要使用manager中的queue  Manager().Queue()

    总共有3个queue  以及各个应用场景
    from queue import Queue
    from multiporcessing import Queue
    from multiprocessing import Manager   Manager().Queue()

    实现进程间共享变量 Manager().dict()

    Pipe只能在两个进程间的通讯   一个是生产者一个是消费者

'''

#使用dis进行查看字节码   gil根据（字节码的行数会进行释放还有就是在遇到io操作）  所以需要再次加锁才能保证公共数据的安全**

import  dis
def add(a):
    a = a +1
    return a

# print(dis.dis(add))


from threading import Thread
from threading import Lock

def get_num():
    pass

Thread(target=get_num,args=()).start()

class MyThread(Thread):

    #可以通过在__init__进行添加参数 在实例中应用上 还有就是记得要引用上父类的方法super().__init__()
    def __init__(self):
        super().__init__()

    def run(self):
        pass

myThread = MyThread()

# myThread.join()   就是保证该线程在主线程完成之前进行结束
# myThread.setDaemon()  这个是保证在主线程运行完才会结束 而不是说不会运行

import time

def demo1(lock):
    time.sleep(2)
    lock.acquire()
    print('demo1')
    lock.release()

def demo2(lock):
    time.sleep(4)
    lock.acquire()
    print('demo2')
    lock.release()


'''
线程池 ThreadPoolExecutor 
'''
#线程池   判断结束   主线程等待
from concurrent.futures import ThreadPoolExecutor,as_completed,wait,FIRST_COMPLETED,Future,ProcessPoolExecutor
#(Future未来对象需要深刻了解一下，task返回容器)

import time

def get_html(times):
    time.sleep(times)
    print('get page {} success'.format(times))
    return times


#  1、对于耗费cpu的操作，多进程优于多线程

def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)

#ThreadPollExecutor和ProcessPollExecutor的接口是一样的
with ProcessPoolExecutor as pe:
    all_task = [pe.submit(fib,(num)) for num in range(20,25)]
    start_time = time.time()
    for future in as_completed(all_task):
        print(future.result())
    print('last use time {}'.format(time.time()-start_time))


#   2、对于IO操作，多线程优于多进程

def random_sleep(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    lock = Lock()
    t1 = Thread(target=demo1,args=(lock,))
    t2 = Thread(target=demo2,args=(lock,))
    # t1.setDaemon(True)
    # t1.start()
    # t2.start()
    # t2.join()
    # time.sleep(3)
    # print(t1.is_alive())
    # print('main')
    executor = ThreadPoolExecutor(max_workers=2)
    #通过submit进行提交 返回一个futures对象  在进行单个提交的时候使用submit
    # futures1 = executor.submit(get_html,(3))
    # futures2 = executor.submit(get_html,(2))
    #通过done来判断是否已运行完成  通过result获取返回值
    # print(futures1.done())
    # print(futures1.result())

    #对多个提交状态的判断使用as_completed
    urls = [3,2,4]
    all_task = [executor.submit(get_html,(i)) for i in urls]
    #使用的时候是as_competed(futures_list)  这个时候返回的是无序的且谁先完成谁返回且获取结果
    # for future in as_completed(all_task):
    #     data = future.result()
    #     print('get {} page'.format(data))

    #使用executor.map 可以直接返回futures.result()的值  且会按照顺序获取结果
    # for data in executor.map(get_html,urls):
    #     print(data)

    wait(all_task,return_when=FIRST_COMPLETED)  #是让主线程等线程池内部的完成，也可以规定几个后进行返回
    print('end')