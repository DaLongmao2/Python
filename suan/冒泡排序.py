#!/usr/bin/env python
# encoding: utf-8
import random

data = [random.randint(1, 9999) for i in range(99999)]
print('代随机的列表: %s ' % data)

for i in range(len(data)):
    for j in range(len(data) - 1 - i):
        if data[j] > data[j+1]:
            data[j], data[j + 1] = data[j + 1], data[j]
print('排序后的有序序列: %s' % data)
