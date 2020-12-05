# 1、产生一个数(1-100), 进行猜测, 如果大了, 说大了, 如果小了小, 直到你猜中为止
import random


def one():
    computer_num = random.randint(1, 100)
    while True:
        try:
            player_num = int(input('请输入一个1-100的数字, 猜大小:'))
            if player_num not in range(1, 101):
                print('请输入1-100内的数字!!!')
                continue
            if player_num > computer_num:
                print('<{}>这个数字大了'.format(player_num))
                continue
            if player_num < computer_num:
                print('<{}>这个数字小了'.format(player_num))
                continue
            print('恭喜你猜中啦这个数字就是:<{}>'.format(computer_num))
            break
        except:
            print('请输入正确的数字类型')


# 2、键盘输入一个数(1-7) 如果为1则为星期一....如果非字符串  友情提示

def two():
    week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']
    while True:
        try:
            num = int(input('几天星期几？    请输入一个数字:'))
            if num not in range(1, 8):
                print('请输入1-7内的数字!!!')
                continue
            print(week[num - 1])
            break
        except:
            print('请输入数字！！！')
            continue


# 3、键盘录入(12321) 判断是不是回数 12121(例子 是) 12365(不是)

def three():
    while True:
        try:
            num = int(input('测试是否为回数？   请输入一个数字:'))
        except:
            print('请输入int类型的数字')
            continue
        str_num = str(num)
        for i in range(0, int(len(str_num) / 2)):
            if str_num[i] != str_num[-i - 1]:
                return print('不是')
        return print('是的')


# 4、求1-100 之前的偶数和
def four():
    even_num = [i for i in range(0, 101, 2)]
    print('1-100之偶数和为 {}'.format(sum(even_num)))


# 5、求1-100 之前的奇数和
def five():
    odd_num = [i for i in range(1, 101, 2)]
    print('1-100之奇数和为 {}'.format(sum(odd_num)))


# 6.判断是否为酒后驾车,要求输入酒精含量判断是否为酒后驾车
# 提示：小于20毫克不构成酒驾，大于或等于20毫克达到饮酒标准，小于80毫克达到饮酒驾驶，大于或等于80，达到醉驾
def six():
    Input = float(input('请输入酒精含量：'))
    if 0 <= Input < 20:
        print('不构成酒驾')
    elif 20 <= Input < 80:
        print('饮酒驾驶')
    elif Input >= 80:
        print('醉酒驾驶')
    else:
        print('请输入正确数值')


# 7.3次密码登录
def seven():
    admin, password = 'admin', '123456'
    c = 3
    while c > 0:
        admin_in = input('请输入账号')
        password_in = input('请输入密码')
        if admin_in != admin and password_in != password:
            c -= 1
            print('输入错误，您还有{}次机会'.format(c))
        else:
            print('登录成功')
            break
    else:
        print('3次用尽')


# 8.键盘录入一个数— 比如 5   结果为 5*4*3*2*1=120    比如 3  结果为 3*2*1 = 6
def eight():
    x = input('请输入一个数字:')
    num = 1
    str_1 = ''
    for i in range(int(x), 0, -1):
        str_1 += str(i)
        num *= i
    print('结果为:{}={}'.format('*'.join(str_1), num))


# 9.woaihopu,hopushiwojia  字符串 大写变小写
def nie():
    string = 'WOAIHOUPU,HOUPUSHIWOJIA'
    print(string.lower())


# 10 [1,8,9,6,5,88]  从大到小排序  从小到大排序
def ten():
    li = [1, 8, 9, 6, 5, 88]
    li.sort()
    print('小—>大', li)
    li.reverse()
    print('大—>小', li)


# 11 [88,77,6,3,5]   max min
def eleven():
    li = [88, 77, 6, 3, 5]
    print('最大', max(li))
    print('最小', min(li))


# 12 利用python 在D 盘 创建文件夹
def twelve():
    import os
    os.mkdir('D:\\利用python在D盘创建文件夹')


# 13 小明1岁生日吹一个蜡烛，2岁吹两个，他突然也不记得，从那一年开始吹，一共吹了几年，妈妈告诉她，一共吹了236个 ，
# 现在问你她是从那一年开始吹，一共吹了多少年？
def thirteen():
    c = 236
    for i in range(1, c):
        x = 0
        for j in range(i, c):
            x += j
            if x == 236:
                print(i)


if __name__ == '__main__':
    seven()
