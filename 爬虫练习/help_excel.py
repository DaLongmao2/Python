# coding = utf-8
import xlwt

workbook = xlwt.Workbook(encoding='utf-8')

worksheet = workbook.add_sheet('sheet1')

for i in range(9):
    for j in range(9):
        worksheet.write(j, i, 'hello')

workbook.save('student.xls')