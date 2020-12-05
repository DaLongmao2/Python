# python 里面存入数据只支持存入  字符串  和  二进制
# json 将Python里任意数据转换为对应的json数据
# pickle 将python里任意对象转换为二进制
import pickle

# 序列化 dumps:将Python数据转换为二进制
#       dump:将Python数据转换二进制，同时保存到指定文件
# 反序列化 loads:将二进制文件加载为Python数据
#         load:读取文件，并将文件的内容加载为Python成为二进制

list1 = [1, 2, 3, 5, '张三', '张三', '张三', '张三', '张三', '张三']

with open('dumps_name.txt', 'wb') as file_dumps:
    x = pickle.dumps(list1)
    file_dumps.write(x)

with open('dump_name.txt', 'wb') as file_dump:
    pickle.dump(list1, file_dump)


with open('dump_name.txt', 'rb') as loads_file:
    x = loads_file.read()
    y = pickle.loads(x)
    print(y)

with open('dump_name.txt', 'rb') as load_file:
    x = pickle.load(load_file)
    print(x)