from matplotlib import pylab
import random

# matplotlib模块默认不支持中文,所以要指定字体
pylab.rcParams['font.sans-serif'] = ['SimHei']

# y轴 x轴 信息
y = [random.randint(20, 35) for i in range(121)]
x = range(0, 121)
# 生成图片信息修改高20宽8 像素80
pylab.figure(figsize=(20, 8), dpi=80)
# 开始绘图
pylab.scatter(x, y)

# 修改x轴信息 并用字符串代取具体的刻度
_x = list(x)
# 实际就是三个列表的累加拼接
_xtick_labels = ['10:{}'.format('0{}'.format(i) if i < 9 else '{}'.format(i)) for i in range(61)]
_xtick_labels += ['11:{}'.format('0{}'.format(i) if i < 9 else '{}'.format(i)) for i in range(61)]
_xtick_labels += ['12:{}'.format('0{}'.format(i) if i < 9 else '{}'.format(i)) for i in range(61)]
# 1分钟一个刻度过于密集 写了3分钟一个刻度

# 修改y轴信息 使y轴数据更加清晰
_y = range(20, 36)
pylab.yticks(_y, ['{}℃'.format(i) for i in _y])

# 刻度尺步长为3 对应的字符串也为3 并且旋转45度
pylab.xticks(_x[::3], _xtick_labels[::3], rotation=45)

# 绘制网格 0.0 - 1.0 清晰度
pylab.grid(alpha=0.1)


pylab.title('2020-10-1号 10:00点--12:00点 三小时温度变化')

# pylab.show()
pylab.savefig('./matp.png')