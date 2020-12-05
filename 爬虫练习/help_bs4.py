from bs4 import BeautifulSoup

file = open('./douban.html', 'rb')

html = file.read().decode('utf-8')

bs = BeautifulSoup(html, 'html.parser')
#
# # 获取网页的title信息
# print(bs.title.string)
# # 获取所有a标签的值
# print(bs.a.attrs)
# # 直接获取整个文档
# print(bs)
# print(bs.name)
# print(bs.attrs)
#
# # 输出注释 不包含注释
# print(bs.a.string)

# ===========================
# 文档遍历
# print(bs.head.contents[1])
print(bs.find_all())

# 文档搜索
