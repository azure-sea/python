# author azure
# 将列表转换成字符串。每个元素之间用_拼接 join
# s= "_".join(["高性价","高频率","道"])
# print(s)
#
# # 将有规律的字符串切割 split
# ss = "高性价_高频率_道"
# print(ss.split("_"))

# lst = ["ps","ae","ai","pr",""]
# # lst.clear()
# for el in lst:   # 有个变量来记录当前循环的位置, 删除第一个元素，第二个元素就占第一元素的位置
#     lst.remove(el)
# print(lst)

# 删除的时候，发现：剩余了一下内容，原因是内部的索引在改变。
# 需要把要删除的内容记录下来。然后循环这个记录。删除原来的列表

# lst = ["ps","ae","ai","pr","au"]
# new_lst = []
# for el in lst:
#     new_lst.append(el)
# # 循环新列表，删除老列表
# for el in new_lst:
#     lst.remove(el)
# print(lst)
# print(new_lst)

# lst = ["张国荣", '张铁林', '张国立', "张曼玉", "汪峰"]
# # 删掉姓张的
# # 记录姓张的.
# zhangs= []
# for el in lst:
#     if el.startswith("张"):
#         zhangs.append(el)
# for el in zhangs:
#     lst.remove(el)
# print(lst)
# print(zhangs)

# 字典
# dic = {"提莫":"冯迪莫","发姐":"陈一发","五五开":"what"}
# # dic.clear()
# lst = []
# for k in dic:
#     lst.append(k)
#
# for el in lst:
#     dic.pop(el)
# print(dic)
# 综上. 列表和字典都不能在循环的时候进行删除. 字典在循环的时候不允许改变大小.

dic = {"apple":"苹果","banana":"香蕉"}
# dic.fromkeys("orange","橘子") # 直接用字典去访问fromkeys不会对字典产生影响
# ret = dict.fromkeys("orange","橘子") #fromkeys 直接使用类名进行访问
# print(dic)

# # 坑1
# a = ["哈哈","呵呵","嗷嗷"]
# ret = dict.fromkeys("abc",a)
# a.append("嘻嘻")
# print(ret)


