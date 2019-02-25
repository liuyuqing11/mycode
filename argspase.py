#-*-coding: utf-8 -*-
import argparse
#python脚本需要从命令行直接读取参数
#python中的命令行解析最简单原始的方法是sys.argv,更高级的玩法是:argparse这个模块(自python2.7开始加入标准库)
#使用方法:导入模块 import argparse
    #调用ArgumentParser()创建解析器对象
    #add_argument()方法指定程序接受的命令参数,执行程序的时候定位参数必选,可选参数可选
        #定位参数:parser.add_argument("echo", help="echo the string")
        #-可选参数(带标签的参数):parser.add_argument("--verbosity", help="increase verbosity")

        #-type:1.指定输入参数的类型;2.表示文件操作的类型从而直接进行文件的读写操作
        #-default:设置默认参数


def main():
    #description参数插入描述脚本用途的信息,可以为空.     :描述程序,add_help:默认是True,可以设置False禁用
    parser = argparse.ArgumentParser(description = "This is a example program")#调用ArgumentParser():创建解析器对象
    #位置参数:出现的第一个参数,赋值给名为echo的键
    parser.add_argument("echo", help = "echo the string")
    #nargs参数限定输入参数的个数,(默认为1)
    #nargs还可以用'*' 表示,若该位置有有参数输入的话,之后所有的输入都将作为该位置参数的值,'+':表示读取至少1个该位置参数.
    parser.add_argument('num', nargs=2, type=int)#表示脚本可以读入2个整数赋予num键(num为数组:[1,2],元素的类型为int)
    #parse.add_argument('num', nargs='*')

    #添加--verbose标签,标签的别名为-v,action:当读取的参数中出现--verbose/-v的时候,参数字典的verbose键对应对应的值为True,help参数用于描述--verbose参数的用途或意义.
    #action参数:表示值赋予键的方式(此例用的是bool类型),action=store_count:将--verbose出现的次数作为verbose的值;action=store_append:每次出现该便签后的值均存入同一个数组再赋值
    parser.add_argument('--verbose', '-v', action='store_true', help='verbose mode')

    #文件的类型
    parser.add_argument('file', type=argparser.FileType('r'))#读取文件
    #设置默认参数
    parser.add_argument('filename', default='text.txt')

    #必需参数:用于确保某些必需的参数有输入
    #required标签说明参数是必需的,且类型为int输入别的类型会报错
    parser.add_argument('--must', '-m', required=True, type=int)
    args = parser.parse_args()
    print("Step 1 print arg[0]: %s" %args.echo)
    print("Step 2 print num : %s" %args.num)

    #test param --verbose
    if args.verbose:
        print("verbose mode on")
    else:
        print("verbose mode off")
if __name__ == "__main__":
    main()