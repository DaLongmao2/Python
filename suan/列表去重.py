#!/usr/bin/env python
# encoding: utf-8
import random

data = [random.randint(1, 10) for _ in range(20)]
print('原始列表 %s ' % data)
x = []
for i in data:
    if i not in x:
        x.append(i)
print('去重后 %s ' % x)

print(list(set(data)))