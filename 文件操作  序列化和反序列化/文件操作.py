# mode:打开文件的模式
# r 只读   w  写入    b 二进制   t 二进制
# 默认是 rt 文本模只读
# encoding 用来指定文件的编码方式  windows系统默认是 gbk
# file = open('xxx.txt')    # 报错 默认是以 rt  打开  如果文件不存在会报错


# file = open('xxx.txt', 'w', encoding='utf-8')
# file.write('你好')

# file = open('xxx.txt', encoding='utf-8')# 默认是rt

# print(file.read())  # 全部读取
# print(file.readline())  # 只读第一行数据

# while True:
#     x = file.readline()
#     print(x)
#     if x == '':
#         break

# 将所有数据读取到列表中去
# print(file.readlines())


# 读取指定的长度
# print(file.read(5))


# mp4 = open(r'D:\Steam\steamapps\workshop\content\431960\2020734772\龙猫山洞.mp4', 'rb')
# print(mp4.read())
#
# while True:
#     x = mp4.read(1024)
#     if not x:
#         break
#     print(x)
#
# file.close()

import os

# 切文件的后缀
# x = input('文件名')
# names = os.path.splitext(x)
# print(names)


# 文件的拷贝
file = input('请输入一个文件的路径')
x = input('请输入新文件的名称')
y = input('请输入新文件的后缀名')
# 判断是否为文件
if os.path.isfile(file):
    old_file = open(file, 'rb')
    new_file = open('{}.{}'.format(x, y), 'wb')
    while True:
        x = old_file.read(1024)
        new_file.write(x)
        if not x:
            break
    old_file.close()
    new_file.close()
else:
    print('文件不存在')

# with open(r'E:\test.txt', 'w', encoding='utf8') as x:
#     x.write('你好')