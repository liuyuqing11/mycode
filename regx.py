import re
#正则：核心观念：正则对象、匹配对象
#regex对象的方法：match、search;
#匹配对象的方法：group、groups:返回包含匹配子组的元祖

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

