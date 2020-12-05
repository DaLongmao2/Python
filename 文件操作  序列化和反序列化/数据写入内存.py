# 将数据写入到内存中涉及到 StringIO  和  BytesIO 两个类
from io import StringIO

x_io = StringIO()
# x_io.write('hello')
# x_io.write(' ')
# x_io.write('word')
# print(x_io.getvalue())


print('hello word', file=open(r'http://a3.att.hudong.com/14/75/01300000164186121366756803686.jpg', 'w'))
print('hello word', x_io)
print(x_io.getvalue())