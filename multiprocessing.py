#要让python实现多进程(multiprocessing),先要了解操作系统相关背景知识
#Unix/Linux操作系统提供了fork()系统调用,其和一般的函数调用相比特殊点在于:普通函数调用一次返回一次,fork()调用一次返回2次
#因为操作系统自动把当前进程(父进程)复制了一份(子进程),然后分别在父进程和子进程内返回.
#有了fork调用,一个进程在接到新任务时就可以=复制出一个子进程来处理新任务
#子进程返回0,父进程返回子进程的ID,----这样做的原因:一个父进程可以fork出很多子进程,父进程需要记下每个子进程id,而子进程只需调用getppid()就可以拿到父进程的ID
#windoes没有fork系统调用

#python的os模块封装了常见的系统调用,其中就包括fork(),可以在python程序中轻松创建子进程啦
import os
print('Process (%s) start....' % os.getpid())

pid = os.fork()
if pid == 0:
    print('I am child process (%s),and my parent is %s.' % (os.getpid(), os.getppid()))

else:
    print('I am parent process (%s) my child process is %s' %(os.getpid(), pid))
    '''
Process (23313) start....
I am parent process (23313) my child process is 23314
I am child process (23314),and my parent is 23313.
    '''

#python是跨平台的,multiprocessing模块是跨平台版本的多进程模块
#在multiprocessing模块提供了Process类来代表一个进程对象
from multiprocessing import Process

#子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)' %(name, os.getpid()))

if __name__ == '__main__':
    print('Parent process is %s' %os.getpid())

    #创建子进程,就是创建Process类的一个实例,(传入一个执行函数和函数的参数),用start()方法启动,join()方法可以等待子进程结束后再继续往下运行,通常用于进程间同步
    p = Process(target = run_proc, args = ('test_child',))
    print('child process was created.')
    p.start()
    p.join()
    print('child process end.')