from openpyxl import Workbook

wb = Workbook()#新建工作簿
ws = wb.active#获取工作表
ws.append(['姓名','学号','年龄'])
ws.append(['张三','1','18'])
ws.append(['李四','2','20'])
wb.save(r'ceshi.xlsx')#保存文件
