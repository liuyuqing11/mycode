#3.python多线程之--ThreadLocal
#ThreadLocal变量是全局变量,每个线程都只能读写自己线程的独立副本,互不干扰.ThreadLocal解决在一个线程中同一个参数在该
# 线程内各个函数间互传的问题.

#具体说明:在多线程环境下,每个线程都有自己的数据(局部变量),线程的局部变量在使用时不必像全局变量那样加锁,
    #但在同一个线程内部进行函数调用时,传递起来麻烦:
def process_student(name):
    #std是局部变量,但每个函数都要使用它,需要将参数传递进去
    std  = Student(name)
    do_task_1(std)
    do_task_2(std)
def do_task_1(std):
    do_sub_task_1(std)
    do_sub_task_2(std)

def do_task_2(std):
    do_sub_task_1(std)
    do_sub_task_2(std)
#每个函数层层调用,传参数太麻烦,因为每个线程要处理不同的Student对象,不能共享(不能用全局变量)
#ThreadLocal应运而生

import threading
#创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    #获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student:
    local_school.student = name
    process_student()

def main():
    t1 = threading.Thread(target = process_thread, args = ('Alice', ), name = 'Thraed-A')
    t2 = threading.Thread(target = process_thread, args = ('Peter', ), name = 'Thraed-B')

    t1.start()
    t2.start()
    t1.join()
    t2.join()
#解释说明:
    #全局变量local_school就是ThreadLocal对象,每个线程对它都可以读写student属性,但线程之间的student属性互不影响
    #人话:local_school可视为全局变量,但该全局变量内的每个属性如:local_school.student都是线程的局部变量,可以任意读写不受干扰
    #也没有管理锁的问题,ThreadLocal内部会处理.
if __name__ == '__main__':
    main()
'''
Hello, Alice (in Thraed-A)
Hello, Peter (in Thraed-B)
'''



