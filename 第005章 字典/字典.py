# author azure
# dic = {'name':'Azure','age':9000} #字符串
# print(dic)

# dic = {1:'a',2:'b',3:"c"}          #数字
# print(dic)

# dic = {True:'1',False:'0'}         #布尔值
# print(dic)

# dic = {(1,2,3):'abc'}              #元组
# print(dic)

#错误示范
# dic = {[1,2,3]:'abc'}              #列表
# print(dic)
# unhashable type: 'list' # 列表不可显示


dic = {'易大师':'剑圣','剑豪':"托儿所","草丛里":"大宝剑"}
# dic['诺手'] = '人头狗' #新增
# print(dic)

dic.setdefault('火女','安妮')  # 如果在字典中存在就不进行任何操作,不存在就进行添加.
dic.setdefault('火女','火男')
print(dic)


# 删 pop del clear

# pop
# ret = dic.pop('易大师')
# print(ret) # 打印被删除键的值.
# print(dic)
# ret = dic.popitem() #随机删除

# del

# del dic['剑豪']
# print(dic)

# clear
dic.clear() #清除全部
print(dic)

# 改:
dic = {'易大师':'剑圣','剑豪':"托儿所","草丛里":"大宝剑"}
dic['剑豪']= '面对疾风'  #强制修改
print(dic)

dic1 = {'火女':'安妮','火男':'布兰德','vn':'暗夜猎手','剑豪':'面对疾风'}
dic1.update(dic)

print(dic1)

# 查
dic1 = {'火女':'安妮','火男':'布兰德','vn':'暗夜猎手','剑豪':'面对疾风'}
for i in dic1:
    print(i)   #for 循环默认是获取字典中的键

print(dic['易大师'])  #查看1  如果key不存在,查询报错
print(dic.get('易大师')) #查看2 如果key不存在 返回 None ,或者dic.get('易大师2','1') key不存在返回1

print(dic.setdefault('易大师')) # 如果key不存在 也返回 None

# keys values items
dic = {'易大师':'剑圣','剑豪':"托儿所","草丛里":"大宝剑"}
print(dic.keys())  # (高仿列表)

for i in  dic.keys():
    print(i)

for i in dic.values():
    print(i)

for i in dic.items():
    print(i)

dic1 = {}
dics = dic1.fromkeys([1,2,3],'abc')
print(dics)

# 字典嵌套:

dic = {
    'name':'晚风',
    'age':43,
    'wife':
        {'name':'郭家庄',
         'age':39,
         'salary':1000
         },
    'baby':[
        {'name':'提莫','age':18},
        {'name':'加上','age':14},
    ]
}

print(dic['baby'][0]['age'])

dic['baby'][0]['age'] = 19
print(dic)
print(dic.get('baby')[0].get('age'))
