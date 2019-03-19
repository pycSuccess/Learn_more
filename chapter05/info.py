#coding:utf-8
'''

深入python的set和dict

1、dict的abc继承关系
    dict是Mapping类型(collections.abc.Mapping)

2、dict的常用方法
    setdefault()  update()等

3、dict的子类(源码是c写的无法走正常继承逻辑）
    不建议继承list和dict等  collections.UserDict     __missing__方法  是否存在key 没有则去找__missing__方法

4、set和frozenset
    集合和不可变集合（无序唯一）
    集合相关的运算 |  &  -

5、dict和set的实现原理 （实现原理相同）
    dict查询的性能远远大于list
    在list中随着list数据的增大，查找时间会增大
    在dict中查找元素不会随着dict的增大而增大

    dict的key或者set的值，都必须是可以hash的
    不可变对象，都是可hash的 str fronzenset tuple 自己的实现的类 __hash__
    dict内存消耗大，但是查询速度快，自定义的对象或者python内部的对象都是用dict包装的
    dict的存出顺序和元素的添加顺序有关
    添加数据有可能改变已有数据的顺序

    实现原理是hash表  计算hash值 有冲突重新计算找到偏移量进行存储

'''
from collections.abc import Mapping,MutableMapping

d = dict()
print(isinstance(d,Mapping))
print(isinstance(d,MutableMapping))


# d.setdefault() 添加进入新值并将该值进行返回
# d.update() 参数的形式 关键字模式  成对的可迭代结构  目的就是将值添加入该字典中


from collections import UserDict

class My_Dict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key,value*3)

my_dict = My_Dict(one=6)  #传入的关键字参数是成对存在的且不需要进行类型转换
my_dict['a']=3
print(my_dict)

s = {'a','d'}
print(type(s))
s.update([1,2,3])
print(s)
