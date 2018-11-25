#1.python给类提供了__call__方法，该方法允许程序员创建可调用的对象（实例），只有定义类的时候实现了该方法，类的实例才能成为可调用的
class C(object):
    def __call__(self, *args):
        print("I'm callable! Called With args are:{}\n".format(*args))


c= C()
c(3) #结果：I'm callable!

#2.布尔函数callable：确定一个对象可否通过函数操作符()来调用
print(callable(dir), callable(c))#True
print(callable('hello'), callable(1))#False

#13.15.2授权
#属性：可以是数据属性，还可以是方法或函数
#对一个已存在的对象（数据类型或是一段代码）进行包装增加新的/删除不要的/修改已存在的功能（功能的改写）
#包装包括定义一个类，该类的实例拥有标准类型的核心行为
#授权是包装的一个特性，可用于简化处理相关命令性功能，实现代码的最大化复用，实现授权的关键点：覆盖__getattr__()方法，在该方法内包含一个对getattr()内建函数
    #调用
    #__getattr__()工作方式：当搜索（引用）一个属性时，任何局部对象首先被找到（python解释器会在局部名称空间中查找，然后在类的名称空间中找）；
    # 否则__getattr__()被调用（搜索对原对象开始授权请求），然后调用getattr()得到对象的一个默认行为。

class WrapMe(object):
    def __init__(self, obj):
        self.__data = obj

    def get(self):
        return self.__data

    def __repr__(self):
        return 'self.__data'

    def __str__(self):
        return str(self.__data)

    def __getattr__(self, attr):
        return getattr(self.__data, attr)

WrappedComplex = WrapMe(3.5+4.2j)
print("复数的虚部={}, 共轭复数={}".format(WrappedComplex.imag, WrappedComplex.conjugate()))#对已有属性的访问通过getattr()方法授权给对象
print(WrappedComplex.get())
