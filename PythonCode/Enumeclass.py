from enum import Enum, unique
#python提供了Enum来实现枚举的功能,枚举class内的每个枚举常亮都是class的唯一一个实例,
#Enum('classname', (name1,name2,...))
#member = classname.name1默认计数从1开始
Month1 = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))#创建Month类型枚举类

#引用枚举类的常亮
print(Month1.Jan)
#枚举其所有成员
#value属性是自动赋值给member(成员)的int常亮,默认计数从1开始
for name, member in Month1.__members__.items():
    print(name, '=>', member, '=>', member.value)#
    '''
Jan => Month.Jan => 1
Feb => Month.Feb => 2
Mar => Month.Mar => 3
Apr => Month.Apr => 4
May => Month.May => 5
Jun => Month.Jun => 6
Jul => Month.Jul => 7
Aug => Month.Aug => 8
Sep => Month.Sep => 9
Oct => Month.Oct => 10
Nov => Month.Nov => 11
Dec => Month.Dec => 12
    '''

#更精准的控制枚举类,可从Enum派生出自定义类
@unique#unique装饰器帮助检查没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
#访问枚举类型
#1.通过通过成员名称访问
print(Weekday.Sun)#类名+成员名
print(Weekday['Sun'])
print(Weekday(0))
print(Weekday.Sun.value)


#元类
#作用:元类是类的模板,控制类的创建行为,先定义metaclass再创建类,metaclass是python面向对象中最难理解的部分

#python的错误处理机制:try..except..else...finally
#将可能出错的代码置于try内, 若执行出错跳转至except,执行完except后(一个except捕获一个异常),执行finally语句(前提:若有)
#python的错误其实也是class,所有的错误类型都继承自BaseException,所以使用except时需要注意的是:它不但捕获该类型的错误,还把其子类也"一网打尽"
#python的所有错误都是从BaseException类派生
try:
    print('try...')
    r = 10 / str('2')
    print('result= ',r)
except ZeroDivisionError as e:
    print('except :', e)
except TypeError as e:
    print('except:', e)
else:
    print('no error!')
finally:
    print('finally finished.')
'''
try...
except : division by zero
finally finished.
'''
    #后话:调用栈,如果错误没有被捕获,他就会一直往上抛,最后被Python解释器捕获,打印错误信息,然后程序退出.

#主动出击:抛出错误
#因为错误是class,捕获一个错误就是捕获到该class的一个实例.因此,错误并不是凭空产生,是通过有意创建并抛出的.自己编写的函数可以抛出很多类型的错误.
#抛出错误首先选择好继承关系,定义一个错误的class,->用raise语句抛出一个错误实例,raise语句如果不带参数,就会把错误原样抛出
class FooError(ValueError):
    pass

def foo(s):
    n =int(s)
    if n==0:
        raise FooError('invalid value: %s' %s)
    return 10 / n
foo('0')





