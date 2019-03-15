#coding:utf-8
'''

深入类和对象

1.鸭子类型和多态  （只要抽象出共同点（魔法函数 函数  方法）就可以使用多态  **不需要继承不需要重写）
            可迭代需要实现 __iter__ 或 __getitem__


2.抽象基类 abc模块
    应用场景：1.检查类是否含有指定的方法 （与反射机制功能同效）判断指定的类就含有对应的方法
                    ps：判断某个对象的类型
                 2.需要强制子类必须实现某个规定方法

    更推荐使用多继承

3.isinstance  和 type 的区别
        isinstance是可以延伸到继承关系的   而type只是对类型id的is判断
        ps: 在无继承关系时候是相同作用 但是存在继承关系的时候 isinstance涉及的范围更大


4.类变量和实例变量

    实例可以调用类变量 而类不可以调用实例变量
    当实例变量与类变量冲突时  实例会自动创建该变量且进行赋值
    使用内置函数 __dict__ 或者 __slots__ 或者 __dir__

5.类和实例属性的查找顺序---mro查找
        特殊情况 菱形  双向开口  c3算法
        广度优先 深度优先

6.静态方法、类方法以及实例方法以及参数相关
    静态方法： @staticmethod 装饰  且无需传必传参数  （不涉及实例不涉及类时使用）
    类方法： @classmethod 装饰 且必须传入类实例 cls  （不涉及实例但是涉及到类时使用）
    实例方法： 无需装饰 但需必须传入实例对象self  （涉及到实例的时候使用）

7.数据封装和私有属性
        双下划线开头__
        通过这种方式可以获取对应的私有属性====》该属性通过实例._类名+属性名   是单下划线类名属性名

8.python对象的自省机制
    自省是通过一定的机制查询到对象的内部结构（向上查找）
    __dict__ __dir__所有属性但是没有属性的值

9.python的super函数 **super真的是调用父类嘛？

    顺序是mro  super().方法名+具体参数

10.mixin继承
    1.mixin类功能单一
    2.不和基类关联但是可以和任意基类组合
    3.在mixin中不要使用super这种用法

11.python的with语句
    关于try except else finally 的运用 没有返回值理解简单
    存在返回值以finally为准 压栈结构
    with是对该功能的优化    __enter__  __exit__ 上下文管理器协议   **（针对的是类）
    contextlib  简化上下文管理器  需要用contextlib.contextmanager装饰     **（针对的是函数）

'''

class Temp:
    def __init__(self,t = (1,2,3)):
        self.t = t

    def __getitem__(self, item):
        return self.t[item]

temp = Temp()
l = [2,3,4,5]
l.extend(temp)
print(l)

import abc
class Use_Abc(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self):
        pass


class Demo(Use_Abc):
    # def get(self):
    #     pass
    pass

#demo = Demo()  #当未进行实例的时候不会进行判定是否实现了抽象方法（在初始化的时候进行检测）


class DemoOne:
    __instance = 10

#实例 点 一个下划线 类名 私有变量名
dem = DemoOne()
print(dem._DemoOne__instance)


class DemoTwo:
    def __enter__(self):   #__enter__内部报错不会继续往下执行
        print('enter')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
    def dosomething(self):  #其他函数报错 __enter__和 __with__均正常执行
        print('dosomething')


with DemoTwo() as dt:
    dt.dosomething()

import contextlib

@contextlib.contextmanager  #装饰器修饰函数
def file_open(file_name):
    print('file open')  #相当于__enter__实现的内容
    yield  #必须存在yield
    print('file close') #相当于__exit__实现的内容

with file_open('name') as fo:
    print('ing')