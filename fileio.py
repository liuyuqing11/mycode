

#1.读文件：3种方式：read\read(N)\readlines()
#with open("test.txt") as confile:
    #line = confile.read()
    #print(line)#返回全文字符串

    #line2 = confile.read(10)
    #print(line2)#返回文件的前10个字符组成的字符串

    #line3 = confile.readline()
    #print(line3)    #[]:返回每行组成的字符串

    #line4 = confile.readlines()
    #print(line4)    #[返回全文每行组成的列表


#2.逐行读取文件：
#每个文件都对应一个文件迭代器
#with open("test.txt") as confile:
    #for line in confile:
        #cc = line.strip()
        #print(cc)

str= "aaa   "
s="bbb"
str1=str.strip()

res1 =str + s
res2 = str1 + s

print("res1={}".format(res1))
print("res2={}".format(res2))