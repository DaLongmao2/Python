import os

file = input('请输入被复制文件的路径:')
# 判断文件是否存在
if os.path.isfile(file):
    path_file = input('请输入新的文件路径:')
    copy_file_name = input('请输入新的文件名称:')
    # 切割文件后缀
    splitext_file_name = os.path.splitext(file)
    # 以二进制打开目标文件
    with open(file, 'rb') as old_file:
        # 以二进制写入文件
        with open('{}{}{}'.format(path_file, copy_file_name, splitext_file_name[1]), 'wb') as new_file:
            while True:
                read_old_file = old_file.read(1024)
                # print(read_old_file)
                new_file.write(read_old_file)
                if not read_old_file:
                    break
    print('复制成功,新文件路径为{}'.format(path_file+copy_file_name+splitext_file_name[1]))
else:
    print('文件不存在')
