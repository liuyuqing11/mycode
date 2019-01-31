import os
#python 高级特性专题
#1.列表生成式:python内置的简单强大的创建list的生成式
    #在写列表生成式时，生成的元素(x*x)要置于前面，后面跟for循环
res1 = [x * x for x in range(1, 11)]
print(res1)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    #for循环可以使用多个变量，列表生成式也可以使用多个变量来生成list
test_d = {"a":"apple", "b":"blue", "c":"con"}
res12 = [ k + '=' + v for k, v in test_d.items()]
print(res12)#['c=con', 'b=blue', 'a=apple']

    #带判断的列表生成式
res2 = [ x * x for x in range(1,11) if x % 2 == 0]
print(res2)#[4, 16, 36, 64, 100]

    #使用2层for循环，生成全排列
res3 = [ m + n for m in "ABC" for n in "XYZ"]
print(res3)#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

    #运用列表生成式列出当前目录下的，所有文件和目录名
res4 = [ d for d in os.listdir('.') ]
print(res4)#['regx.py', 'classlearn.py', 'fileio.py', 'lambda.py', 'pythondatatype.py', 'pltdrawing.py', 'gaoji.py', 'plt绘图', '.git']


#2.生成器：由于内存限制，列表容量有限，对于一个大的列表想在用到时再生成。不必创建完整list，节省大量空间,在python中此种 "---边循环边计算---" 的机制称为生成器：generator
#生成器是可迭代对象,保存的是算法
    #创建生成器的方法一:将列表生成式的[]->()
    #通过next()函数得到生成器计算的下一个返回值,到最后一个元素没有更多元素时,抛出StopIteration异常(不人性化的方式)
    #因为是可迭代对象,可用for循环,获得生成器返回值,不需要关心StopIteration异常
g = (x *x for x in range(10))
print(type(g), next(g))#<class 'generator'> 0
for i in g:
    print(i)#1,4,9,16,25,36,49,64,81

    #创建生成器的方法二:函数中包含yield关键字,这个函数就变成生成器了
    #变成生成器的函数,每次调用next()时执行,遇到yield语句返回,再次执行时从上次返回的yield语句处执行
    #用生成器实现斐波那契数列演算
def fib(max):
    n, a, b = 0, 0,1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return "done"
g2 = fib(6)
while True:
    try:
        x = next(g2)
        print("g:", x)
    except StopIteration as e:
        print("generator return value is:", e.value)
        break
"""
g: 1
g: 1
g: 2
g: 3
g: 5
g: 8
generator return value is: done
"""

#迭代器VS可迭代对象
#( 可迭代对象 )
#可用于for循环的对象统称为可迭代对象-Iterable:1.集合数据类型(list tuple dict set str);2.生成器(生成器 带yield的 generator function)
#Iterabls对象的判断:Iterable([], Iterable):True False
#( 迭代器)
#可被next()方法调用并不断返回下一个值的对象称为迭代器:Iterator
#迭代器对象的判断:isinstance((x for x in range(10)), Iterator)
#可用于for循环,可被next()函数调用返回计算值,到最后可抛出StopIterator错误(表示无法继续返回下一个值)
#python的迭代器对象表示的是一个数据流,迭代器对象可被next()方法调用并不断返回下一个数据,直到没有数据时抛出StopIterator异常.
#这个数据流可看做是一个有序序列,但该序列的长度却不能提前预知,只能不断通过next()按需计算下一个数据,所以Iterator的计算是惰性的,只在需要返回下一个数据时才会计算.
#迭代器可以表示一个无限大数据流,但列表却不能(如全体自然数)

#从Iteartable(list str dict) 转换为Iterator:iter()函数----iter([])

##summary
#可迭代对象:凡是可用于for循环的对象
#迭代器:可用于next()函数的对象,表示一个具有惰性计算能力的序列
#集合数据对象可通过iter()函数获得一个迭代器
#python的for 循环本质上就是通过不断调用next()函数实现的



