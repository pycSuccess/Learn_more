#coding:utf-8
'''

对象引用、可变性和垃圾回收
1、python中的变量是什么？
    便利贴思想  先生成对象 之后将变量贴在对象上

2、==和is的区别
    ==是比较值
    is是比较id()是否相等  判断的是身份
    ps：python也存在常量池 小整数 小字符串

3、del语句和垃圾回收
    del不是直接回收而是要gc机制触发引用计数为0的进行清理操作
    重写__del__

4、一个经典的参数错误 （传入默认的可变数据结构会造成数据混乱不唯一）
    参数在传入默认可变数据结构时  会造成多个对象均使用一个默认可变参数造成数据的错乱问题
'''

class Demo:
    def __init__(self,name,li=[]):
        self.name = name
        self.li = li  #li是每次创建实例对象的时候将引用赋值给实例变量li 所以对于可变数据结构来说就会出现多次引用修改等
        self.drivers = [] #而这个drivers是每次实例的时候都会重洗赋值一个新的空list

    def add(self,x):
        self.li.append(x)
        self.drivers.append(x)

    def remove(self,x):
        self.li.remove(x)
        self.drivers.remove(x)

demo = Demo('demo',[1,2,3,4])
# print(demo.li)
# print(demo.drivers)
demo.add(5)
demo.add(7)
demo.remove(7)
#打印li和drivers 查看值的变化
demo2 = Demo('demo2')
demo2.add(3)
demo2.add(4)
print(demo2.li,id(demo2.li))
print(demo2.drivers,id(demo2.drivers))
demo3 = Demo('demo3')
print(demo3.li,id(demo3.li))
print(demo3.drivers,id(demo3.drivers))