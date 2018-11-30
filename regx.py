import re
#正则：核心观念：正则对象、匹配对象
#regex对象的方法：match、search;
#匹配对象的方法：group、groups

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



