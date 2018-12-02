import re
#正则：核心观念：正则对象、匹配对象
<<<<<<< HEAD
#regex对象的方法：match（匹配）、search（搜索）|findall（搜索）、sub|subn（搜索替换）、split（分割）;
#匹配对象的方法：group、groups:返回包含匹配子组的元祖
#原始字符串:raw strings
=======
#regex对象的方法：match、search;
#匹配对象的方法：group、groups:返回包含匹配子组的元祖
>>>>>>> 1d9f0f145baec3ec3bfdf672a51d0676e616143b

#一、正则表达式对象的方法
#1.match：从字符串开始对模式进行匹配，匹配成功返回匹配对象，失败返回None
    #match(pattern, string, flags=0)
m1 = re.match('foo', 'footest!')
if m1 is not None:
    print("Match Success,result is:{}".format(m1.group()))#Match Success,result is:foo

m2 = re.match('foo', 'not start with foo')
if m2 is not None:
    print("Match Success.result is:{}".format(m2.group()))
else:
    print("Match Fail.")#Match Fail.

#2.search():在字符串的任意位置对模式进行匹配
m_sea = re.search('foo', 'not start with foo')
if m_sea is not None:
    print('search success, the result is:{0}'.format(m_sea.group(0)))#search success, the result is:foo


#3.正则对象的搜索函数之二findall()：搜索成功-返回匹配结果列表；搜索失败-空列表（与search不同不返回匹配对象）
m3_1 = re.findall('car', 'scary')
m3_2 = re.findall('car', 'carry the barcard to the car!')
m3_3 = re.findall('car|the', 'carry the barcard to the car!')
print("findall result is:{0}、{1}、{2}".format(m3_1, m3_2, m3_3))#findall result is:['car']、['car', 'car', 'car']、['car', 'the', 'car', 'the', 'car']

#4.正则对象的搜索替换函数：sub、subn：
    #sub(1,2,3):返回替换处理后的字符串
    #subn(1,2,3)：返回元组（替换处理后的字符串、替换次数）
print(re.sub('X', 'Mr.Smith', 'X\n\nDear X, \n'))
    #Mr.Smith

    #Dear Mr.Smith,
print(re.subn('X', 'Mr.Smith', 'X\n\nDear X, \n'))
    #('Mr.Smith\n\nDear Mr.Smith, \n', 2)


#5.re模块的分割函数：split
from os import popen
from re import split

f= popen('who', 'r')
for eachLine in f.readlines():
    print(split('\s\s+|\t', eachLine.strip()))#\s\s+：至少两个空格

f.close()
#['liuyuqing :0', '2018-11-29 23:28 (:0)']
#['liuyuqing pts/0', '2018-11-30 21:22 (:0)']
#['liuyuqing pts/3', '2018-12-02 11:01 (:0)']
#['liuyuqing pts/4', '2018-12-02 11:02 (:0)']


#用match、search匹配多个字符串

multi_str_pattern = 'bat|bet|bit'
    #match
multi_match1 = re.match(multi_str_pattern, 'bat')
if multi_match1 is not None:
    print("Yes Matched:{0}".format(multi_match1.group()))#Yes Matched:bat

    #search
multi_match2 = re.search(multi_str_pattern, 'test not start with bat.')
if multi_match2 is not None:
    print("Yes Matched:{0}".format(multi_match2.group()))
else:
    print("match fail.")#Yes Matched:bat


#二、匹配对象的group及groups方法
g1 = re.match('(\w\\w\w)-(\d\d\d)', 'adc-123')
if g1 is not None:
    print("group match resulr:{0},type is:{1}.len is:{2}".format(g1.group(), type(g1.group()), len(g1.group())))#group match resulr:adc-123,type is:<class 'str'>.len is:7
    print("group result :{0}\{1}".format(g1.group(0), g1.group(1)))#adc-123\adc,返回了匹配的子组字符串

if g1 is not None:
    print("groups result is:{0},type is:{1},len is:{2},greops result[1] is {3}".format(g1.groups(), type(g1.groups()), len(g1.groups()),\
                                                                                       g1.groups(3))) #groups result is:('adc', '123'),type is:<class 'tuple'>,len is:2,greops result[1] is ('adc', '123')
<<<<<<< HEAD

#三、原始字符串
#产生原因：ASC2字符和正则表达式特殊字符间所产生的冲突：
    #如：\b:退格键，匹配一个单词的边界，解决：用\转义但麻烦，或者用r简化
r_1 = re.match('\bblow', 'blow')#None
r_2 = re.match(r'\bblow', 'blow')
=======
>>>>>>> 1d9f0f145baec3ec3bfdf672a51d0676e616143b

print("r_1.group={0},r_2.group()={1}".format('None', r_2.group()))#r_1.group=None,r_2.group()=blow
