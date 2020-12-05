# 序列化：将数据从内存话持久化报错到硬盘的过程
# 反序列化：将数据从硬盘加载到内存的过程

# write时只能写入字符串或者二进制
#   1、将数据转换为字符串: repr()/str()   使用json模块
#       json 本质就是字符串，区别在于json里要用双引号表示
#   2、将数据转换为二进制:  pickle模块
import json
# 序列化
# dumps 将数据转换为字符串，不会保存到文件里
# dump  将数据转换为字符串，同事保存到指定文件

file = open('name.txt', 'w', encoding='utf8')
name = ['zhang', 'yyy', 'ff']
name1 = ('zhang', 'yyy', 'ff')
# file.write(str(name)) # 直接转换为str

# x = json.dumps(name)  # dumps 将数据转换为字符串，不会保存到文件里
# file.write(x)

json.dump(name1, file)  # dump  将数据转换为字符串，同事保存到指定文件

file.close()


# json 反序列化
# loads: 将json字符串加载成为Python里的数据
# load: 读取文件,把文件的内容加载成为Python里的数据

str_x = '{"name": "zhangyi", "age": 18}'
one = json.loads(str_x)
print(one)
print(type(one))

two = open('name.txt', 'r', encoding='utf8')
two_1 = json.load(two)
print(two_1)

