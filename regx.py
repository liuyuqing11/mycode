import re
#正则：核心观念：正则对象、匹配对象

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


