# coding = utf-8
from matplotlib import pylab

a = [15, 15, 19, 21, 27, 33, 35, 39, 39]
b = [29, 35, 41, 41, 34, 41, 41, 35, 29]

a1 = [15, 27, 39]
b1 = [29, 13, 29]

pylab.plot(a, b, color='red')
pylab.plot(a1, b1, color='red')


x = range(51)
y = range(51)
pylab.xticks(x, rotation=90)
pylab.yticks(y)

pylab.grid()
pylab.show()
