#coding:utf-8
'''

元类编程

1、property动态属性
        就是将实例方法变成实例属性 @property
    @属性名.setter 是设置值时书写的方法

2、__getattr__ getattribute__ 魔法函数

    __getattr__ 是在获取不到属性的时候调用该方法**

    __getattribute__ 是在获取到与获取不到都会调用的方法（当抛出异常的时候会去调用重写的__getattr__)

3、属性描述符和属性查找过程

    优先级又高到低：   __getattribute__ --> 属性数据描述符 （类属性=class()）-->__init__ -->非数据描述符--> 类属性

    如果user是某个类的实例，那么user.age(以及等价的getattr(user,'age')
    首先调用__getattribute__。如果类定义了__getattr__方法，
    那么在__getattribute__抛出AttributeError的时候就会调用到__getattr__
    而对于描述符(__get__)的调用，则是发生在__getattribute__内部的
    user = User() ,那么user.age 顺序如下：
    1.如果age是出现在User或其基类的__dict__中，且age是data descriptor，那么调用其__get__
    2.如果age出现在obj的__dict__中，那么直接返回obj.__dict__['age']否则
    3.如果age出现在User或其类的__dict__中
    3.1.如果age是no-data descriptor，那么调用其__get__方法，否则
    3.2.返回__dict__['age']
    4.如果User有__getattr__方法，调用__getattr__方法，否则
    5.抛出AttributeError

4、__new__（组装类：控制对象的生成过程） 和 __init__(组装对象：完善对象) 区别和理解
    ps:如果new方法不返回对象，则不会调用__init__

5、自定义元类  （做检查 预先准备）
    type动态创建类  类名  (继承关系)  {类属性 方法}
    元类继承type   使用类参数metaclass=元类  通过元类来控制使用类的实例化过程
    ps：元类会控制继承该类的子类甚至更深的子类  先查看本身再向上查找

6、通过元类实现orm
        通过元类进行对参数进行校验 orm就是通过类对象操作数据的一条数据
        class User:
            name = CharField(db_column= '' ,max_length= 10)
            age = IntField(db_column = '' ,min_value = 0,max_value = 100

            class Meta:
                db_table = 'user'

'''
from datetime import datetime,date
class Demo:

    def __init__(self,birthday,info={}):
        self.birthday = birthday
        self.age = self._age
        self.info = info
    @property
    def _age(self):
        return datetime.now()

    @_age.setter
    def _age(self,value):
        self._age = self.birthday + value

    def __getattr__(self, item):
        return self.info[item]   #当前例子就是在没有name的属性的时候 会调用__getattr__方法来进行逻辑处理

    def __getattribute__(self, item):  #不管有没有该属性都会直接调用__getattribute__的方法  是控制类实例流程的内部函数
        return '无条件执行'             #ps：甚至将__init__里面的赋值都忽略到



demo = Demo(11,info={'name':'aaaa'})
demo.age = 33
print(demo.age)
print(demo._age)
print(demo.name)


class UserMeta(type):
    def __new__(cls, *args, **kwargs):
        print('Usermeta')
        return super().__new__(cls,*args,**kwargs)  #此处是因为委托给metaclass进行创建 所以要将参数都传入过去  记得要返回一个类实例

class User(metaclass=UserMeta):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def __str__(self):
        return self.name

user = User('名字')



'''
通过元类进行实现orm


'''

#这样就能更好的使用isinstance

class MyField:
    pass

#metaclass的类一定要继承type这样才会拥有创造类的功能  同时可以进行控制类的创建流程 但要注意的是
#在重写__new__方法的时候一定要进行返回一个实例这样才能进行__init__方法进行丰富实例

class MyMeta(type):
    def __new__(cls, name,bases,attrs,**kwargs):
        fields = {}
        for key,value in attrs.items():
            if isinstance(value,MyField):
                fields[key] = value
        attrs['fields'] = fields
        return super().__new__(cls, name,bases,attrs)


#父类使用metaclass是为了能够 进行实例的时候不至于更改子类的__init__方便拓展  同时可以向上抽象出其他操作方法

class BaseClass(metaclass=MyMeta):
    def __init__(self,*args,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
        super().__init__()

    def save(self):
        for key,value in self.fields.items():
            print(key)


#通过数据描述符 来控制该类中内部参数的限制  同时在设置和获取的时候进行格式要求
#将两个数据描述符的类进行继承一个基类是为了能够更好地根据类型取出该值

class MyStr(MyField):
    def __init__(self):
        self._value = None
    #     self.name = name

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = value

class MyInt(MyField):
    def __init__(self):
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = value

class UserProfile(BaseClass):
    name = MyStr()
    age = MyInt()
    class Meta:
        pass

up = UserProfile(name='mqy',age=12)
#print(UserProfile.__dict__)
#print(up.__dict__)
#up.name = 12
#print(up.name)
up.save()