

#在各种程序中都有配置文件,python中引入了configParse模块进行操作.
#配置数值类型:bool型\整数型\在操作时都是字符串类型

#配置文件的三种定义:
    #1.section:章节   注意:大写的[DEFAULT]的基类其下面所有新增的章节,都会继承这个(后面章节不写option)都会继承这个章节.
    #2.option:选项. 是每一个章节的定义
    #3.value:选项的值

import configparser
import os
#1)基本的写入配置文件
    #(1)add_section(section):添加一个新的章节
    #(2)set(section,option, valeu):对section中的option进行设置,需要调用write将内容写入配置文件,注意在
    #调用set()之前需要先调用add_section增加一个新的章节
#step1:生成一个configparser对象
conf = configparser.ConfigParser()

#step2:生产一个章节,必需先定义一个字典
conf['DEFAULT'] = {}
conf['DEFAULT']['base_dir'] = '/home/lyq02/data'
conf['DEFAULT']['max_items'] = '1000'

conf['test2'] = {}
conf['test2']['use_gpu'] = 'True'

base_dir = r'/home/liuyuqing/PCode/test'
path = os.path.join(base_dir, 'common.ini')

conf.add_section('test3')
conf.set('test3','is_student','True')

#step3:写入到文件中
with open(path, 'w') as f:
    conf.write(f)#对conf文件进行io


print(conf.get('test3','is_student'))
print(conf.get('test3','is_student'))
#2)基本的读取(查看)配置文件:
    #read(filename)
    #sections():得到所有的section,以列表形式返回,默认大写的DEFAULT是不返回的(DEFAULT是默认的基类,下面所有的都会继承这个属性,,类似继承)
    #options:(section):得到该section的所有option
    #items(section):得到该section的所有键值对
    #get(section, option):得到section中的option值,返回值为string类型
    #getint(section, option):得到section中option值,返回为int类型,相应的还有getboolean()和getfloat()


conf2 = configparser.ConfigParser()
conf2.read('/home/liuyuqing/PCode/test/common.ini')#直接读取文件内容
sections = conf2.sections()
print("type of sections is :{0} values is :{1}".format(type(sections), sections))
#type of sections is :<class 'list'> values is :['test2']
opts = conf2.options('test2')
print("type od conf.options return is :{0}, value is:{1}".format(type(opts), opts))
#type od conf.options return is :<class 'list'>, value is:['use_gpu', 'base_dir', 'max_items']

print(conf2.items('test2'))#[('base_dir', '/home/lyq02/data'), ('max_items', '1000'), ('use_gpu', 'True')]
print(conf2.get('test2', 'base_dir'))#/home/lyq02/data




