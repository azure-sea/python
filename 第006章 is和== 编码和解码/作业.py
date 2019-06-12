# author azure
# 1, 有如下变量(tu是元组),请实现要求的功能.
# tu = ("alex",[11,22,{"k1":'v1',"k2":['age',"name"],"k3":(11,22,33)},44])
#a讲述元组的特性
#a. 只读列表不可改变.

#b. 请问tu变量中的第一个元素"alex" 是否可被修改?
##不可以
#c. 请问tu变量中的"k2"对应的值是什么类型? 是否可以被修改? 如果可以,请在其中添加一个元素"Seven"
# 列表  可以   append添加
#d. 请问tu变量中的"k3"对应的值是什么类型? 是否可以被修改? 如果可以,请在其中添加一个元素"Seven"
# 元组  不可以

#2. 字典dic = {'k1':"v1",'k2':"v2",'k3':[11,22,33]}

#a 请循环输出所有的key
dic = {'k1':"v1",'k2':"v2",'k3':[11,22,33]}
for i in dic.keys():
    print(i)

#b. 请循环输出所有的value
for i in dic.values():
    print(i)

#c. 请循环输出所有的key和value
for i in dic.items():
    print(i)

#d. 请在字典中添加一键值对,"k4":"v4",输出添加后的字典.
dict = {'k1':"v1",'k2':"v2",'k3':[11,22,33]}
dict['k4'] = 'v4'
print(dict)

#e. 请在修改字典中"k1"对应的值我"alex", 输出修改后的字典.
dic = {'k1':"v1",'k2':"v2",'k3':[11,22,33]}
dic['k1'] = 'alex'
print(dic)

#f. 请在k3对应的值中追加一个元素 44, 输出修改后的字典
dic = {'k1':"v1",'k2':"v2",'k3':[11,22,33]}
dic['k3'].append(44)
print(dic)

#g. 请在k3对应的值中第一个位置插入个元素18, 输出修改后的字典.
dic = {'k1':"v1",'k2':"v2",'k3':[11,22,33]}
dic['k3'].insert(0,18)
print(dic)

#3. 有字符串"k:1|k1:2|k2:3|k3:4" 处理成字典{'k':1,'k1':2,'k2':3,'k3':4}
s = "k:1|k1:2|k2:3|k3:4"
new_li = s.split("|")
dic = {}
#print(new_li)
for i in new_li:
    k,v=i.split(":")
    dic[k] = int(v)
print(dic)


#4 有如下值li = [11,22,33,44,55,66,77,88,99,90],将所有大于66的值保存至字典的第一,
#  即: {'k1':大于66的值列表,'k2':小于66的值列表}
li = [11,22,33,44,55,66,77,88,99,90]
dic = {'k1':[],'k2':[]}
for i in li:
    if i == 66:
        continue
    elif i > 66:
        dic.setdefault('k1').append(i)
    else:
        dic.setdefault('k2').append(i)
print(dic)
