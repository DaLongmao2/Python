# coding = utf-8
import time
from selenium import webdriver
import parsel

# 实例化浏览器驱动 传入浏览器驱动
bro = webdriver.Chrome(executable_path=r'/home/zhangyi/chromedriver')

# 让浏览器发起一个指定url对应请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')

# page_source 获取浏览器当前页面的页面源码的数据
page_text = bro.page_source

# 转换为 Selector 对象
tree = parsel.Selector(page_text)
li_list = tree.xpath("//div[@id='FileItems']//li")
for li in li_list:
    name = li.xpath('./dl/@title').get()
    print(name)

time.sleep(5)
# 退出驱动
bro.quit()