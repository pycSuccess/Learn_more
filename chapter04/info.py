#coding:utf-8
'''

自定义序列类
1、python中的序列分类
    容器序列 ：list tuple duque
    扁平序列：str bytes bytearray array.array
    可变序列：list deque bytearray array
    不可变：str tuple bytes

2、序列的abc继承关系 collections.abc    in操作是实现了__contains__


3、序列的+ +=和extend的区别
        + 对参数有要求必须是相同类型  而+= 对格式没有要求原理就是extend方法  对可迭代对象进行for取值进行append


4、实现可切片的对象
    对切片操作  取值 赋值（赋值时是一个iterater）  删除
    slice是切片对象如[:]

5、bisect维护已排序序列
    用来处理已排序的序列  始终维护一个已排序结构必须是可修改的


6、什么时候我们不该使用列表
    引用array和deque在不同场景也许是更好的选择

7、列表推导式、生成器表达式、字典推导式
    列表推导式:[]  可以代替map reduce filter
    生成器表达式:()
    字典推导式:{}

'''

l = [1,3,4]
l+={'a':1}
print(l)

#这种赋值与+=操作一致  都是对后面的进行遍历之后再append进去（insert进去）
l[:2] = (8,9)
print(l)
l[:0] = [0]
print(l)
print((1,2,3,4)[0:1])

import numbers

class Demo:

    def __init__(self,stf):
        self.stf = stf

    def __getitem__(self, item):
        if isinstance(item,slice):  #判断是切片还是取值（[:] [num])  这个是判断是否是切片
            pass
        elif isinstance(item,numbers.Integral): #判断是否是num值
            pass

    def __iter__(self): #返回的是一个迭代器对象 iterator
        return iter(self.stf)


#array 和 deque
from array import array   #存放指定数据类型（对类型有限制）
my_array = array('i') #不同的类型所用的值存在不同的标志符
my_array.append(3)
my_array.append(4)
print(my_array)
#my_array.append('3') 必须是添加相同类型的数据



d1 = {'a':2,'b':3,'c':4}
d2 = {v:k for k,v in d1.items()}  #字典推导式 对key和value进行位置颠倒
print(type(d2))
sorted(d2)
print(d2)
my_set = {k for k,v in d1.items()}
print(my_set)
print(type(my_set))



