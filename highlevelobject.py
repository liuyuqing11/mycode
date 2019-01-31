#定义一个类并创建该class 的实例后,可以给该实例动态绑定任何属性和方法,注意给一个实例动态绑定属性和方法对另一个实例不起作用
class Student(object):
    pass

stu1 = Student()
stu1.name = "Michale"#动态给实例绑定属性
print(stu1.name)#Michale

def set_age(self, age):
    self.age = age
from types import MethodType
stu1.set_age = MethodType(set_age, stu1)#动态的给实例绑定一个方法
stu1.set_age(20)
print(stu1.age)#20

#为了实现给所有实例都绑定属性和方法,可以给类绑定方法,
def set_scores(self, score):
    self.score = score
Student.set_scores = set_scores

stu2 = Student()
stu3 = Student()
stu2.set_scores(22)
stu3.set_scores(23)
print("stu2.age={0},stu3.score={1}".format(stu2.score,stu3.score))#stu2.age=22,stu3.score=23

##1.限制类实例的属性,只能给实例添加规定的属性:使用特殊变量__slots__
#__slots__属性在子类中不起作用,除非子类中也定义__slots__属性
class Student_strict(object):
    __slots__ = ("name", "age")#tuple定义允许实例绑定的属性
ss1 =Student_strict()
#ss1.aa = 2#试图绑定未定义的属性,将引发AttributeError
#print(ss1.aa)#AttributeError: 'Student_strict' object has no attribute 'aa'

class Student_strict_son(Student_strict):
   # __slots__ = ()#除非子类也定义了__slots__属性
    pass

sss = Student_strict_son()
sss.aa = 2
print(sss.aa)


#2.定制类:__xxx__的变量和函数在Python 中有特殊用途
    #2.1__str__与__repr__
    #__str__打印实例时给出好看的结果,print(实例)返回用户看到的字符串,__repr__:返回程序开发者看到的字符串,直接打印实例
class Test1(object):
    pass
t1 = Test1()
print(t1)#<__main__.Test1 object at 0x7f36c6c7c710>
class Test1_1(object):
    def __init__(self, name):
        self.name = 'test1'
    def __str__(self):
        return 'Test1_1 object (name = %s)' %self.name
    __repr__ = __str__

t1_1 = Test1_1("Test1_1")
print(t1_1)#Test1_1 object (name = test1)

    #2.3__getattr__():__getattr__()方法:当调用的属性/方法不存在时,python解释器会试图调用__getattr__()来尝试获得属性,这样就有机会动态返回一个属性/方法
    #实质:把一个类的属性和方法调用全部动态化处理了
    #当调用类的属性和方法时,若不存在则报错:AttributeError
class Test2(object):
    pass
t2 = Test2()
#print(t2.age)#AttributeError: 'Test2' object has no attribute 'age'

class Test2_1(object):
    def __getattr__(self, attr):
        if attr=='name':
            return "Somebody"
        if attr=="age":#支持返回函数
            return lambda:22
        raise AttributeError('class \'Test2_1\' object has no attribute \'%s\'' %attr)
t2_1 = Test2_1()
print(t2_1.name)
print(t2_1.age())




