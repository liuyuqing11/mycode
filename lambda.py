#lambda关键字用于创建匿名函数对象（匿名函数：不以def这种标准方式来声明的函数，该对象不会在任何名称空间内创建名字）
#lanbda表达式返回可调用的对象
#lambda函数不像C++的内联函数其存在不是为了节约性能（绕过函数的栈分配），而是被调用时创建一个框架对象

#1.一个关于单行函数的例子
def true():return True
print(true()) #True

true1 = lambda  :True
print(true1()) #True

#2.1带参数的lambda函数
add1 = lambda x,y :x+y
print(add1(2,3)) #5

#2.2带默认参数的lambda函数
add2 = lambda x,y=0 : x+y
print("add2(1)={0},add2(1,2)={1}".format(add2(1),add2(1,2))) #1,3

#3.带多个参数的lambda表达式
mul = lambda *args : args#(此处args随便起的)
print(mul(1,2,3))#(1,2,3)

print(mul([1,2,3],"cc" ))#([1, 2, 3], 'cc')




