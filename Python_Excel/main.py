# 导包
import xlrd

data = xlrd.open_workbook("/home/zhangyi/2019级新生分班（电子信息学院）_咸职0925.xls")

table = data.sheet_by_name('剔除厚溥')


nrows = table.nrows
ncols = table.ncols

for i in range(nrows):
    print(table.row_values(i))