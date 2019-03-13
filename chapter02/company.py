#coding:utf-8
class Company:
    def __init__(self,employee_list):
        self.employee_list = employee_list

    #是实现切片操作的魔法函数（协议）item传递的是index 字典不可进行该迭代
    #如何实现 将emlloyee_list传入的是字典也能直接进行对类做切片操作
    def __getitem__(self, item):
        #print(item)
        #return self.employee_list[item]
        return self.employee_list[item]

company = Company([1,2,3,4])
#company = Company({'a':1,'b':2,'c':3})
for item in company:
    print(item)


class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x+other.x ,self.y+other.y)

    def __str__(self):
        return (self.x,self.y)

v1 = Vector(1,2)
v2 = Vector(3,4)
print(v1+v2)