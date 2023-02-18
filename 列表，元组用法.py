a = ['hell', 'hello', 'hello', 'hello', 'hello', 'hello']
#元组自动拆包
for index,value in enumerate(a): #enumerate，按索引遍历
    if value == 'hello':
        print(index)
# for i in range(len(a)): #按下标遍历
#     # print(i)
#     if a[i] == 'hello':
#         print(i)

# a1 = ("11", "22", "33", "44", "55")
# k, *_, v = a1
# print(k)
#
## *args 将值放入一个元组，*kargs 将值放入一个字典，前提是有键值对的
# def abc(a,b,c,*args,**kwargs):
#     print(f'a:{a}')
#     print(f'b:{b}')
#     print(f'c:{c}')
#     print(f'*args:{args}')
#     print(f'*kwargs:{kwargs}')
# abc(1,2,3,4,5,aa='bb')