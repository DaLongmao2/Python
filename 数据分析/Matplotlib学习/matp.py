# coding = utf-8
from matplotlib import pylab as plt


plt.figure(figsize=(20, 8), dpi=200)
# 数据在 x 轴的位置,是一个可迭代对象(加产生[2, 4, ..., 24]12个索引的列表)
x = range(2, 26, 2)

# 数据在 y 轴的位置, 必须是一个可迭代对象(对应x轴产生12个值的列表)
y = [15, 13, 16, 5, 17, 15, 17, 15, 16, 18, 80, 55]

# 传入 x, y 绘制 折线图
plt.plot(x, y)

# 传入 x y 的 轴的刻度
# plt.xticks(range(1, 26))
plt.yticks(range(1, 101, 5))

# 更加精准 使用列表推导式
plt.xticks([i/2 for i in range(1, 49)], rotation=45)

# 显示图形
# plt.show()

# 保存图片
plt.savefig('./matp.png')