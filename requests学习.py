import requests
import json
from openpyxl import Workbook
# 新冠数据url
url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
# 使用reqests中的get方法获取数据并存储在一个变量
result = requests.get(url=url)
# 获取到的数据是json格式，需要导包json，获取想要的字段
data = result.json().get('data')
"""
获取到的数据是str类型，需要转换成json格式，使用json.loads()来转换，
load和loads的区别是loads里面直接str转换成字典，load将json格式的字符转换为dict，从文件中读取 
"""
t = json.loads(data)
#获取字典中想要的字段
chinaDayList = t.get('chinaDayList')
chinaDayADDList = t.get('chinaDayADDList')
sum= {}#新建一个大字典
#循环chinaDayList字典取出所有值
for i in chinaDayList:
    nian = i.get('y')
    yue = i.get('date')
    #用replase将字符改变
    yue = yue.replace('.', '-')
    confirm = i.get('confirm')
    suspect = i.get('suspect')
    dead = i.get('dead')
    heal = i.get('heal')
    dat = nian + '-' + yue
    # ws.append([dat,confirm,suspect,dead,heal])
    # print(f'{dat} 确诊人数：{confirm} 疑似人数：{suspect} 死亡人数：{dead} 治愈人数：{heal}')
    sum[dat]={'确诊人数':confirm,'疑似人数':suspect,'死亡人数':dead,'治愈人数':heal}
# print(sum)
for i in chinaDayList:
    nian = i.get('y')
    yue = i.get('date')
    #用replase将字符改变
    yue = yue.replace('.', '-')
    confirm = i.get('confirm')
    suspect = i.get('suspect')
    dead = i.get('dead')
    heal = i.get('heal')
    dat = nian + '-' + yue
    # ws.append([dat,confirm,suspect,dead,heal])
    # print(f'{dat} 新增确诊人数：{confirm} 新增疑似人数：{suspect} 新增死亡人数：{dead} 新增治愈人数：{heal}')
    sum[dat].update({'新增确诊人数': confirm, '新增疑似人数': suspect, '新增死亡人数': dead, '新增治愈人数': heal})
# print(sum)

wb = Workbook()#新建工作簿
ws = wb.active#获取工作表
ws.append(['时间','确诊人数','疑似人数','死亡人数','治愈人数','新增确诊人数','新增疑似人数','新增死亡人数','新增治愈人数'])
#字典.items()方法可以把字典转换成一个（key，value）元组的列表
for k,v in sum.items():
    ws.append([k,v['确诊人数'],v['疑似人数'],v['死亡人数'],v['治愈人数'],v['新增确诊人数'],v['新增疑似人数'],v['新增死亡人数'],v['新增治愈人数']])
#
wb.save(r'ceshi.xlsx')
# print(result.json())
#
#
