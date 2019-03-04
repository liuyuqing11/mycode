import numpy as np
import matplotlib.pyplot as plt

#基础:
#1.# plt.figure():使用figure命令产生多个图,图片号按顺序增加.在绘图中有2个重要概念当前图和当前坐标,所有绘图操作仅对当前图和当前坐标有效
#2.plt.plot(x, y, format_string, **kwargs)
    #x轴数据,y轴数据、format_string:控制曲线的格式字符串(由颜色|风格字符|标记字符组成)
    #1.颜色字符'b'蓝色 'g':绿色 'r':红色 'c':青绿色 'm':洋红色 'k':黑色 'y':黄色 'w':白色
    #2.风格字符:'-':实线 '--':破折线 '-.':点画线 ':':虚线


x1 = np.arange(-5.0, 5.0, 0.02)
x2 = np.arange(-5.0, 5.0, 1)
y1 = np.sin(x1)
y2 = np.cos(x2)

plt.figure(1)
plt.subplot(211)
plt.plot(x1, y1)

#设置坐标范围plt.axis([xmin, xmax, ymin, ymax])
plt.subplot(212)
plt.axis([-2.5, 2.5, -1, 1])
#xlim(-2.5, 2.5)
#ylim(-1, 1)
plt.plot(x1, y1)

#叠加曲线
fig2 = plt.figure(2)
plt.subplot(3, 3, 3)
plt.plot(x1, y1, 'm-.', x2, y2, 'g^')



plt.figure()
mu, sigma = 100, 15
x3 = mu + sigma * np.random.randn(10000)

#画数据直方图

n, bins, patches = plt.hist(x3, 50, normed=1, facecolor='g', alpha=0.75)

#plt.text(): 在图的任意位置添加文字,并支持LaTex语法
#plt.xlabel('str') plt.ylabel('str'):用于添加x轴和y轴标签
#plt.title(''):添加图的题目
plt.xlabel('Smarts')
plt.ylabel('Probality')
plt.title('History of IQ')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)


#plt设置图例
#给图添加图注plt.legend()
    #参数:loc-图例的位置
    #edgecolor:图例边框颜色\facecolor:图例背景色,frameon = False:去掉图例边框
plt.figure()
p1,  = plt.plot([1,2,3])
p2,  = plt.plot([3,2,1])
plt.legend([p1, p2], ["line1", "line2"], loc = 'upper right', edgecolor = 'blue')
plt.show()



