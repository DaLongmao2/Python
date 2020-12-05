# #!/usr/bin/env python
# # encoding: utf-8
# from selenium import webdriver
# import pymysql
# import os
# import time
#
#
# class XiaoYuanWang:
#     user_list = []
#     passwd_list = []
#     t = time.localtime()
#     sql = "DELETE FROM `Sheet1` WHERE `学号` = '{}';".format(user_list[i])
#     db = pymysql.Connect(host='localhost', port=3306, passwd='1122', db='xiaoyuanwang', user='root', charset='utf8')
#     cursor = db.cursor()
#
#     def execute_sql_select(self, sql):
#         self.cursor.execute(sql)
#         for data in self.cursor.fetchall():
#             self.user_list.append(data[0])
#             self.passwd_list.append(data[1][-6:])
#
#     def save_login(self, username, passwd):
#         with open('校园网可用账号密码.txt', 'a+', encoding='utf-8') as fp:
#             fp.write("保存于：{}年{}月{}日{}时{}分{}秒 \t 账号：{} \t 密码：{}  \n".format(
#                 self.t[0], self.t[1], self.t[2], self.t[3], self.t[4], self.t[5], username, passwd
#             ))
#
#
#     def save_del(self, username, passwd):
#         with open('已从数据库删除账号密码.txt', 'a+', encoding='utf-8') as fp:
#             fp.write("删除于：{}年{}月{}日{}时{}分{}秒 \t 账号：{} \t 密码：{}  \n".format(
#                 self.t[0], self.t[1], self.t[2], self.t[3], self.t[4], self.t[5], username, passwd
#             ))
#
#
#     def save_failure(self, username, passwd):
#         with open('流量超支账号密码.txt', 'a+', encoding='utf-8') as fp:
#             fp.write("超支于：{}年{}月{}日{}时{}分{}秒 \t 账号：{} \t 密码：{}  \n".format(
#                 self.t[0], self.t[1], self.t[2], self.t[3], self.t[4], self.t[5], username, passwd
#             ))
#
#
#     def get_url(self):
#         for i in range(len(self.user_list)):
#             driver = webdriver.Chrome(executable_path=r"/home/zhangyi/chromedriver")
#             # driver.maximize_window()
#             driver.get('http://192.168.255.100/0.htm')
#
#             username = driver.find_element_by_id('username')
#             password = driver.find_element_by_id('password')
#             button = driver.find_element_by_id('submit')
#
#             username.click()
#             username.clear()
#             username.send_keys(self.user_list[i])
#
#             password.click()
#             password.clear()
#             password.send_keys(self.passwd_list[i])
#
#             button.click()
#             try:
#                 error_text = driver.find_element_by_xpath('//*[@id="info"]').text
#
#                 if error_text == '账号或密码不对，请重新输入':
#                     print('登录失败，user:《{}》passwd:《{}》 账号密码错误'.format(self.user_list[i], self.passwd_list[i]))
#                     self.cursor.execute(self.sql)
#                     self.save_del(self.user_list[i], self.passwd_list[i])
#                     print("已从数据库删除")
#
#                 elif error_text == '本账号费用超支或时长流量超过限制':
#                     self.cursor.execute(self.sql)
#                     self.save_failure(self.user_list[i], self.passwd_list[i])
#                     print('登录失败，改账户 user:《{}》passwd:《{}》 流量超支'.format(self.user_list[i], self.passwd_list[i]))
#
#             except:
#                 print('登录成功，user:《{}》passwd:《{}》'.format(self.user_list[i], self.passwd_list[i]))
#                 self.save_login(self.user_list[i], self.passwd_list[i])
#                 break


if __name__ == '__main__':
    import threading
    import time

    def index():
        print('我日')
        time.sleep(3)
        print('..')


    t1 = threading.Thread(target=index)
    t2 = threading.Thread(target=index, name='线程2', group=None)
    t3 = threading.Thread(target=index, name='线程2', group=None)
    t4 = threading.Thread(target=index, name='线程2', group=None)
    t5 = threading.Thread(target=index, name='线程2', group=None)
    t6 = threading.Thread(target=index, name='线程2', group=None)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

