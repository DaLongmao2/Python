# 匹配出163的邮箱地址,且@符号之间有4列到20位(可以为数字,字母,下划线,必须英文开头),例如 hello@163.com
import re


def main():
    input_em = input('请输入您的163邮箱:')
    re_em = re.match(r'[a-zA-Z][a-zA-Z0-9_]+@163.com', input_em)
    if re_em:
        print('输入正确')
    else:
        print('输入有误')

if __name__ == '__main__':
    main()




