#coding:utf-8
'''

1、python 中一切皆对象

函数和类也是对象，属于python的一等公民

ps:    特性
    1、赋值给一个变量
    2、可以添加到集合对象中去
    3、可以作为参数传递给函数
    4、可以当做函数的返回值

2、type object class的关系
    1.继承关系  所有类都继承object 但是object没有基类
    2.创建关系 所有对象都是有type创建的 包括它自己
    ps：type创建了万物包括type和object
        object是所有类的基类 但是不包括自己

3.python中的常见内置类型
    1.对象的三大特征： 身份 id  类型 type  值 value

    类型： None 全局只有一个
            数值：int float complex复数 bool
            迭代类型：
            序列类型：list tuple str array range （bytes bytearray memoryview)
            映射类型；
            集合类型：set frozenset   （性能高）
            上下文管理类型：with
            其他：模块类型  class和实例 方法类型 代码类型 object对象 type类型 elipsis类型（省略号） notimplemented类型

'''