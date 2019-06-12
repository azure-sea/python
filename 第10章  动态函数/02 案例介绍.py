# author azure
#2. 写函数，
# 检查获取传入的列表或元组对象的所有奇数位索引对应的元素，
# 并将其作为新列表返回给调用者。
# #         0        1      2     3      4       5
# lst = ["皇阿玛","纯妃","香妃","贵妃","皮妃", "咖啡"]
# def func(lst):
#     result = []
#     for i in range(len(lst)):
#         if i%2 == 1: # 奇数位的索引
#             result.append(lst[i])
#     return result
# ret = func(["皇阿玛","纯妃","香妃","贵妃","皮妃", "咖啡"])
# print(ret)

# 方式二：
# lst = ["皇阿玛","纯妃","香妃","贵妃","皮妃", "咖啡"]
# def func(lst):
#     return lst[1::2]
# print(func(lst))

# 3. 写函数,判断用户传入的对象(字符串、列表、元组) 长度是否大于5
# def func(a):
#     return len(a) > 5
# print(func("我写的很少啊"))

# 4. 写函数，检查传入列表的长度，如果大于2，
#   将列表的前两项内容返回调用者.
# def func(a):
#     if len(a) > 2:
#         #return a[0],a[1]
#         return a[0:2]
#
# print(func("我写的很少啊"))

# 5. 写函数,计算传入函数的字符串中
#  数字、字母、空格 以及 其他内容的个数，并返回结果。
# def func(s):
#     shuzi = 0
#     zimu = 0
#     kongge = 0
#     qita = 0
#     for i in s:
#         if i.isdigit():
#             shuzi += 1
#         elif i.isalpha(): #
#             zimu +=1
#         elif i == ' ':
#             kongge += 1
#         else:
#             qita +=1
#     return shuzi, zimu ,kongge, qita
# print(func("as dfqjsfas asifasdf123a awe1$$$"))

# 6. 写函数，接收两个数字参数，返回比较大的那个数字
# def func(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# a = 40
# b = 20
# c = a if a >b else b  # 三元表达式 如果a 大于b 返回if前面的数 反之 返回else后面的数
# print(c)

# 通过三元表达式进行对函数优化
# def func(a,b):
#     return a if a >b else b
# set = func(10,20)
# print(set)

# 7.  写函数，检查传入字典的每一个value的长度，如果大于2,
#  那么仅仅保留前两个长度的内容，并将新内容返回给调用者，
#    dic = {"k1":"vlue1","k2":[11,22,33,44]}
#    PS: 字典中的value只能是字符串或列表

# def func(dic):
#     newdic = {}
#     for k, v in dic.items():
#         if len(v) > 2:
#             s = v[0:2]
#             newdic[k] = s
#         else:
#             newdic[k] = v
#     return newdic
# print(func({"jey":"周杰伦","潘婷":"洗发水","票容":"自傲与啊","伊卡璐":"卡卡江苏省"}))

# 8. 写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成功能是返回给调用者一个字典
#   此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回词典为 {0:11,1:22,2:33}

# def func(lst):
#     if type(lst) == list:
#         dic = {}
#         for i in range(len(lst)):
#             dic[i] = lst[i]
#         return dic
#     else:
#         return "不是列表."
# print(func(["自作孽","不可活","脱壳","加壳"]))


# lst = [11,22,33]
# print(type(lst))  # type()返回的是类型
# print(list)    # list 列表类型

# 9. 写函数, 函数接收四个参数分别是：姓名、性别、年龄、学历。
#  用户通过输入这四个内容，然后将四个内容传入到函数中，
#  此函数接收到这四个内容，将追加到一个student_msg文件中。

# def func(name,gender,age,edu):
#     with open("student_msg", mode="a", encoding="utf-8") as f:
#         f.write(name+"_"+gender+"_"+age+"_"+edu+"\n")
# name = input("请输入名字:")
# gender = input("请输入性别:")
# age  = input("请输入年龄:")
# edu = input("请输入学历:")
# print(func(name,gender,age,edu))

# 10. 对9进行升级: 支持用户持续输入，Q或者q退出，默认性别为男，

# def func(name,age,edu,gender="男"):
#     with open("student_msg", mode="a", encoding="utf-8") as f:
#         f.write(name+"_"+gender+"_"+age+"_"+edu+"\n")
# while 1:
#     content = input("是否开始录入学生信息(按Q退出): ")
#     if content.upper() == 'Q':
#         break
#     else:
#         name = input("请输入名字:")
#         gender = input("请输入性别:")
#         age  = input("请输入年龄:")
#         edu = input("请输入学历:")
#         if gender == "":
#             func(name,age, edu)
#         else:
#             func(name, age, edu, gender)

# 11  写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作.
# import os
# def func(filename,old,new):
#     with open(filename,mode="r",encoding="utf-8") as f1,\
#         open(filename+"_副本",mode="w",encoding="utf-8") as f2:
#         for line in f1:
#             line = line.replace(old, new)
#             f2.write(line)
#     os.remove(filename)
#     os.rename(filename+"_副本", filename)
# func("11题test","开始","结束")


# 12 写一个函数完成三次登陆功能,在写一个函数完成注册功能

# # 非常函数功能
# count = 1
# while count <=3:
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#     if username == "azure" and password == '123':
#         print("登陆成功")
#         break
#     else:
#         print("用户名或密码错误")
#         print("当前尝试了%s次" % count)
#     count = count +1

# # 函数方式
# def login():
#     count = 1
#     while count <=3:
#         username = input("请输入用户名:")
#         password = input("请输入密码:")
#         if username == "azure" and password == '123':
#             print("登陆成功")
#             return
#         else:
#             print("用户名或密码错误")
#             print("当前尝试了%s次" % count)
#         count = count +1
# login()

# 12 写一个函数完成三次登陆功能,在写一个函数完成注册功能()
#    注册：
#        首先. 要从文件中读取用户名和密码,匹配用户输入的用户名和文件中的用户名是否一致.如果一致,提示重新输入
#        其次. 如果上面到判断没有问题, 把用户名和密码写入文件中
