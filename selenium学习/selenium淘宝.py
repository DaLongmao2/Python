# coding = utf-8
from selenium import webdriver
from time import sleep
from lxml import etree

# pro = webdriver.Chrome("E:/chromedriver/chromedriver.exe")
pro = webdriver.Chrome("/home/zhangyi/chromedriver")
pro.get("https://www.taobao.com/")
pro.maximize_window()  # 窗口最大化

search_input = pro.find_element_by_id("q")
search_button = pro.find_element_by_css_selector("#J_TSearchForm > div.search-button > button")
search_input.clear()
search_input.send_keys("美食")
search_button.click()

sleep(2)
login_username = pro.find_element_by_css_selector("#fm-login-id")
login_password = pro.find_element_by_css_selector("#fm-login-password")
login_button = pro.find_element_by_css_selector("#login-form > div.fm-btn > button")
login_username.send_keys("大龙猫1124")
login_password.send_keys("@ZhangYi520")
login_button.click()

selector = etree.HTML(pro.page_source)
div_list = selector.xpath('//*[@id="J_Itemlist_Pic_625988389426"]/@src')
print(div_list)
sleep(5)
pro.quit()
