# author azure
#lst = ["赵四","施瓦辛格","海波","郭大侠","赛利亚"]
# 在后面添加
#lst.append("黄宏") # 在原有的基础上进行的操作
# 在前面添加
#lst.insert(1,"王力宏") #在1位置插入

# lst.extend("马化腾") # 迭代添加 单字加
# lst.extend(["马云","王健林"]) #整个加
# print(lst)

# 删除
# data = lst.pop(2) #返回被删除的数据
# print(data)
# print(lst)
# lst.remove("赵四") #删除元素
# lst.remove("刘能") #如果不存在即报错"x not in list"

#切片删除
#del lst[1:3]

#清空
# lst.clear()
# print(lst)

# lst = ["王者荣耀","魔兽世界","DNF","你受寒","cs"]
# # lst[0] = "扫雷" #替换"王者荣耀"为"扫雷".
# # lst[1:3] = ["跑跑卡丁车"]  # 先删除在追加
# lst[1::2] = ["qq华夏","QQ三国"] #切片的时候.如果步长不是1.注意元素的个数
# print(lst)

lst = ["锅包肉","火锅","烤鱼","白菜","烤鸭"]

for el in lst:  #element(元素)
    print(el)