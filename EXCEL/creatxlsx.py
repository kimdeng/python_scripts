#coding=utf-8
import xlsxwriter

workbook=xlsxwriter.Workbook('demo.xlsx')
worksheet=workbook.add_worksheet()
chart=workbook.add_chart({type,'area'})
worksheet.set_column('A:A',20)
bold=workbook.add_format({'bold':True})
worksheet.write('A1','HELLO')
worksheet.write('A2','world',bold)
worksheet.write('B2',u'中文测试',bold)
worksheet.write(2,0,32)
worksheet.write(3,0,35.5)
worksheet.write(4,0,'=SUM(A3:A4)')
worksheet.insert_image('B5','test.jpg')
worksheet.insert_chart('A15',chart)
workbook.close()