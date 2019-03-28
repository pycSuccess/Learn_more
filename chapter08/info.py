#coding:utf-8
'''

迭代器和生成器

1、python的迭代协议

    迭代器是什么？  迭代器是访问集合内元素的一种方式，一般用来遍历数据
    迭代器和以下标的访问方式不一样，迭代器是不能返回的，迭代器提供了一种惰性方式
    实现__iter__就是可迭代对象 该方法会返回一个迭代器
    实现__iter__和__next__是迭代器对象

    from collections.abc import Iterable Iterator

2、什么是迭代器和可迭代对象

        通过iter()可以返回一个iterator
        next()方法进行获取到下一个值
        StopIteration next的截止标识就是抛出该异常且只能抛出该异常

3、生成器函数使用

    生成器函数只要有yield （不是一个普通的函数） 返回的是一个生成器对象（python编译字节码的时候就产生了）
    通过生成器实现斐波那契

4、生成器的原理 **

    使用dis.dis可以获取对象的字节码
    python一切皆对象，栈帧对象，字节码对象
    当foo调用子函数bar 又会创建一个栈帧
    所有的栈帧都是分配在堆内存（不释放不会销毁）上的，这就决定了栈帧可以独立于调用者存在

5、通过UserList来看生成器的应用


6、生成器实现大文件的读写

    使用到read（长度）  通过yield

'''

'''
针对2 书写的事例
'''
from collections.abc import  Iterator

#首先要在实现迭代协议的类中进行实现__iter__方法 且返回的是一个迭代器（该迭代器不应该是本身是其他迭代器）
class Company:
    def __init__(self,employee_list):
        self.employee_list = employee_list

    def __iter__(self):
        return MyIterator(self.employee_list) #通过第三方的迭代器进行处理且返回该迭代器对象

class MyIterator(Iterator):
    def __init__(self,employee_list):
        self.employee_list = employee_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):  #在实现__next__的方法时  一定要抛出StopIteration
        try:
            work = self.employee_list[self.index]
        except Exception as e:
            raise StopIteration
        self.index+=1
        return work


com = Company([1,2,3,4])
# for i in com:  #首先先返回一个迭代器对象  之后进行next赋值给i
#     print(i)

'''
针对3
'''
#取固定位置的值
def fib(index):
    if index<=2:
        return 1
    else:
        return fib(index-1)+fib(index-2)  #会保存上一个的值 之后进行增加
#print(fib(10))

#打印出所有的值
def g_fib(indx):   #不要轻易使用数据结构 这样就会消耗内存 当数据增大的时候会加剧内存的消耗
    a,b = 0,1
    while indx>0:   #在使用yield的时候实现循环遍历值一定要使用while
        yield b       #会保存起来 但是需要在进行计算的时候才会产生值
        a,b = b,a+b
        indx-=1

# for i in g_fib(10):
#     print(i),

'''
针对4
'''
name = 'mqy'
def gen_func():
    yield 1                      #是运行到第一个yield为止，执行之前的代码且将yield的值返回出来（执行逻辑）
    print('yield 1')
    yield 2
    global name
    name = 'mqy 666'
    return 'return....'   #暂时未发现在生成器函数中添加return后有什么用

g = gen_func()
# for i in g:
#     print(i)
# print(name)
# print(g)

'''
针对6
'''

def myreadline(f,newline):
    buf = ''
    while 1:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos+len(newline)]
        chunk = f.read(4096)
        if not chunk:
            yield buf
            break
        buf += chunk