#高阶函数Higher-order function

#函数式编程:函数名作为参数,函数名的实质:函数名就是指向函数的变量(变量可以指向函数)
#高阶函数:一个函数可以接收另一个函数作为参数,或返回函数这样的函数就叫做高阶函数(函数的参数能够接收别的函数)
#高阶函数的抽象能力非常强大,使得核心代码可以保持非常简洁
#python内建了map和reduce函数

#1.高阶函数map:
    #map作为高洁函数把运算规则抽象化了,一眼就可以看出对序列中的每个元素进行了什么样的操作
    #map(函数对象f(运算规则,映射函数), Iterable)
    #Return:Iterator(惰性序列)
def multi(x):
    return x * x

res1 = []
print(type(map(multi, [x for x in range(4)])))#<class 'map'>
res1 = list(map(multi, [x for x in range(4)]))#使用list()获得所有结果,并返回list
print(res1)#[0, 1, 4, 9]

#2.高阶函数reduce(累积运算)
    #reduce(f, Iteratable):f(x,y):必须有2个参数!
from functools import reduce
def add(x, y):
    return x + y
res2 = []
res2 = reduce(add, [1,2,3])
print(res2)

#3.高阶函数fileter:关于保留和丢弃
    #filter(f, Iterablde):f:筛选函数,返回值为bool型,
    #Return:Iterator(惰性序列)
    #filter函数依据返回值来决定保留还是丢弃序列中的元素
res3 = []
    #保留奇数
res3 = list(filter(lambda x: x%2, [0,1,2,3,4]))
print(res3)

#4,高阶函数sorted:排序算法
    #4.1非高阶用法:用sort实现序列排序,不改变原序列的值
origin = [-3,3,1,-9,0]
sorted_origin = sorted(origin)
print("排序后的序列为:{}".format(sorted_origin))#排序后的序列为:[-9, -3, 0, 1, 3]

    #4.2sorted函数的高阶用法:sorted([list], key = f. reverse = True)传入参数key = f(映射函数):用f实现对序列元素预处理,处理后再排序,排序的关键在于实现一个映射函数,reverse:反向排序功能开关
sorted_abs = sorted(origin, key = abs)
print("按绝对值排序的结果为:{}".format(sorted_abs))#按绝对值排序的结果为:[0, 1, -3, 3, -9]

    #4.3用sorted实现忽略大小写的排序
name_list = ["Han Meimei", "Xiao ming", "xiaohong", "adraw"]
name_sorted = sorted(name_list, key = str.lower, reverse = True)
print("逆序排序后的名单为:{}".format(name_sorted))#逆序排序后的名单为:['xiaohong', 'Xiao ming', 'Han Meimei', 'adraw']

#5.高阶函数-装饰器decorator
    #decorator返回函数的高阶函数,不修改原来函数的定义在代码运行期间动态增加功能的方式,称之为装饰器decorator
    #函数对象有一个__name__属性,可以拿到函数的名字.

    #5.1定义一个能打印日志的装饰器
def log(func):#log是一个装饰器,其参数是一个函数,返回值也是一个函数
    def wrapper(*arg, **kw):#wrapper函数可以接受任意参数的调用
        print('call %s():' %func.__name__)
        return func(*arg, **kw)
    return wrapper
    #使用装饰器:借助python的@语法,把装饰器置于函数的定义处=执行now函数时,实际执行了log(now)
@log
def now():
    print("2019-01-28")

now()
'''
call now():
2019-01-28
'''
import functools # 导入functools模块
    #5.2若decorator本身需要传入一个参数,需要定义一个返回decorator 的高阶函数(自定义log文本),3层嵌套的装饰器
def log2(text):
    def decorator(func):
        @functools.wraps(func) #实现func.__name__函数名属性传递只需在wrapper函数的定义前加@functools.wraps(func)
        def wrapper(*arg, **kw):
            print("%s %s():" %(text, func.__name__))
            return func(*arg, **kw)
        return wrapper#返回wrapper函数
    return decorator#返回装饰器
@log2("execute")
def now():
    print("2019-01-28")

now()#=log2("execute")(now)最终返回函数wrapper
print(now.__name__)#wrapper
'''
execute now():
2019-01-28
'''
    #不需要编写wrapper.__name__=func.__name__:python内置的functools.wraps就是做这件事的






