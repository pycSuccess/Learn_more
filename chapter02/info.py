#coding:utf-8
'''

魔法函数

**不是通过类继承获取的而是类本身进行扩展的
定义： 双下划线开头并且以双下划线结尾的函数


分类一、非数学运算
    字符串表示
        __repr__  __str__
    集合、序列相关
        __len__  __getitem__ __setitem__ __delitem__ __contains__
    迭代相关
        __iter__ __next__
    可调用
        __call__
    with上下文管理器
        __enter__ __exit__
    数值转换
        __abs__ __bool__ __int__ __float__ __hash__ __index__
    元类相关
        __new__ __init__
    属性相关
        __getattr__ __setattr__ __getattribute__ __setattribute__ __dir__
    属性描述符
        __get__ __set__ __delete__
    协程
        __await__ __aiter__ __anext__ __aenter__ __aexit__

    **使用len进行处理的数据结构使用内置类型计算时速度非常快  是走捷径不是来遍历

    **for循环在被遍历的对象未实现迭代器协议来返回迭代器对象时 就会走__getitem__魔法函数 进行走切片逻辑



'''