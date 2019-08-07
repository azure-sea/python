# author azure

# 2. 写函数,接收n个数字,求这些参数数字的和。(动态传参)
#  方式一：
# def func(*args):
#     sum = 0
#     for i in args:
#         sum = sum +i
#     return sum
# print(func(1,5,7))

# 方式二:
# def func(*args):
#     return sum(args)
# # print(sum([1,5,7]))  # sum中可以直接接受一个可迭代对象. 他会把这个可迭代对象进行迭代,把每个元素累加。
# print(func(1,2,3,4))

# 3. 读代码,回答: 代码中打印出来的值a,b,c 分别是什么？为什么？
# a = 10
# b = 20
# def test(a,b):
#     print(a,b)
# c = test(b,a)
# print(c)
# a=20 b=10 c=None

# 4. 读代码,回答: 代码中打印出来的值a,b,c 分别是什么？为什么？
# a = 10
# b = 20
# def test(a,b):
#     a = 3
#     b = 5
#     print(a,b)   # a=3,b=5
# c= test(b,a)
# print(c)   #None
# print(a,b)    # a=10, b=20

# 5. 写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元组,集合等),
# 将每个实参的每个元素依次添加到函数的动态参数args里面
# 例如: 传入函数两个参数[1,2,3](22,33)最终args为(1,2,3,22,33)

# def func(*args):
#     print(args)
# func(*[1,2,3],*(22,33))

# 6.写函数，传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs里面.
# def func(**kwargs):
#     return kwargs
#
# ret = func(**{"name":'a'},**{"age":'b'},**{"bs":"c"},)
# print(ret)

# 7. 判断下面代码是否成立
# # 7.1  结果为 2
# a = 2
# def wrapper():
#     print(a)
# wrapper()

# # 7.2  结果为 ERROR
# a = 2
# def wrapper():
#     # global a  #局部访问全局中的变量。结果为3
#     a +=1
#     print(a)
# wrapper()

# # 7.3  结果为2
# a = 2
# def wrapper():
#     def inner():
#         print(a)
#     inner()
# wrapper()

# # 7.4  结果为Error
# def wrapper():
#     a = 1
#     def inner():
#         # nonlocal a  # 外层函数中离他最近的变量 a
#         a +=1
#         print(a)
#     inner()
# wrapper()

# 8. 写函数，接收两个数字参数,将较小的数字返回.
# def  func(a,b):
#     return a if a < b else b
# set = func(9,7)
# print(set)

# 9. 写函数, 接收一个参数(此函数类型必须是可迭代对象),将可迭代对象的每个元素以"_"相连，
# #    形成新字符串,并返回.
# def  func(lst=[1, "alex", "wusir"]):
#     s = ""
#     for el in lst:
#         s =s + str(el) + "_"
#     return s.rsplit("_")
#
# print(func())


# 10. 写函数,传入n个数, 返回字典{'max':最大值,'min':最小值}
#    例如:min  max(2,5,7,8,4) 返回{'max':8,'min':2}
# print(max(1,5,7,8,123,2))
# print(max([1,5,7,8,123,2]))

# def func(*args):
#     return {'max':max(args),'min':min(args)}
# print(func(1,2,3,4,4,5))


# 11. 写函数，传入一个参数n, 返回n的阶乘。
#    例如:cal(7) 计算 7*6*5*4*3*2*1
# def func(n):
#     sum = 1
#     while n >=1:
#         sum = sum * n
#         n = n -1
#     return sum
# print(func(5))

# 12. 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
#    例如: [('红心',2),('草花'),2],...('黑桃','A')]  # 笛卡尔积

# def func():
#     result = []
#     huase= ["红心","黑桃","草花","方片"]
#     dianshu = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
#     for hua in huase:
#         for dian in dianshu:
#             result.append((hua,dian))
#     return result
#
# print(func())

# 13. 有如下函数:
# def wrapper():
#     def inner():
#         print(666)
# wrapper()
# 你可以添加任意代码,用于两种或以上的方法,执行inner函数。

# 方式一
# def wrapper():
#     def inner():
#         print(666)
#     return inner()
# wrapper()
#
# def wrapper():
#     def inner():
#         print(666)
#     return inner
# ret = wrapper()
# ret()
# print(ret)

#  14  九九乘法表


# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%sx%s=%s" % (i,j,i*j),end=" ")
#     print() # 打印空 换行

#  1.  登陆功能
# def regist():
#     print("欢迎进入注册系统")
#     while 1:
#         username = input("请输入用户名:").split()
#         password = input("请输入密码:").split()
#         if username == "" or password== "":
#             print("用户名或密码不合法")
#             break
#         # 校验用户名是否存在
#         f = open("db.log",mode="r",encoding="utf-8")
#         for line in f:
#             if username == line.split("@@")[0]:
#                 print("该用户名已注册")
#                 break
#         else: #未注册过
#             f.write("\n"+username+"@@"+password)
#             print("注册成功")
#             return
# regist()

