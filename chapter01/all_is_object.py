#coding:utf-8


'''

简单实例操作

'''


def ask():
    print('ask')
    return 'sssss'

ask1 = ask

class MyClass:
    def __init__(self):
        print('myclass')

myclass = MyClass
myclass()

ask1()

for item in [ask,myclass]:
    print(item())

print('==========')
def get_func(fun):
    print(fun.__name__)
    return fun()

print(get_func(ask))


def get_fun(fun):
    print(fun.__name__)
    return fun

ask_ =  get_fun(ask)
# ask_()
print(ask_)


'''

type和object和class的关系

'''

class Demo:
    pass

print(type(Demo))
print(Demo.__bases__)
print(type(type))
print(object.__bases__)
print(type(object))