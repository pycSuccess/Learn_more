#coding:utf-8
'''

深入类和对象

1.鸭子类型和多态  （只要抽象出共同点（魔法函数 函数  方法）就可以使用多态  **不需要继承不需要重写）
            可迭代需要实现 __iter__ 或 __getitem__


2.抽象基类 abc模块
    应用场景：1.检查类是否含有指定的方法 （与反射机制功能同效）判断指定的类就含有对应的方法
                    ps：判断某个对象的类型
                 2.需要强制子类必须实现某个规定方法
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

demo = Demo()  #当未进行实例的时候不会进行判定是否实现了抽象方法（在初始化的时候进行检测）