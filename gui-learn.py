#python gui 学习
#Tk是python的默认GUI库,它基于tk工具集(Tkinter_默认GUI库,tk-默认工具集)

#创建GUI程序总共5步:
    #1,导入tkinker模块:import tkinter/ fro tkinter import *
    #2.创建顶层窗口对象,容纳整个GUI程序
    #3.在顶层窗口对象上,创建所有的gui模块(功能)
    #4.把GUI模块与底层程序代码相连接
    #5.进入主事件循环

#tk有2个坐标管理器来协助把

import tkinter

top = tkinter.Tk()#TK是tkinter内的一个类,调用该类创建一个顶层窗口对象(搭画架)
label = tkinter.Label(top, text='Hello World!')
label.pack()
tkinter.mainloop()