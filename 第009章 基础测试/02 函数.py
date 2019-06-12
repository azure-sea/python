# author azure

# 定义了一个动作或功能
# def yue():
#     print("1")
#     print("2")
#     print("3")
#     print("4")
#     print("5")
# # 应用
# yue()

#  return 使用一：
# def yue():
#     print("1")
#     print("2")
#     print("3")
#     return
#     print("4")
#     print("5")
#
# se = yue()
# print(se)

# #  return 使用二(返回值)：
# def yue():
#     print("1")
#     print("2")
#     print("3")
#     return "stop"
#     print("4")
#     print("5")
# se = yue()
# print(se)


#  return 使用三(多返回值)：
# def yue():
#     print("1")
#     print("2")
#     print("3")
#     return "stop","shutdown",'init 0'
#     print("4")
#     print("5")
# se = yue()
# print(se)

# 写函数。让用户输入a和b ，返回a+b的结果
# def sum():
#     a = int(input("请输入一个a:"))
#     b = int(input("请输入一个b:"))
#     c = a+b
#     return c
# ret = sum()
# print("结果为：%d " % ret)

# 在函数声明的位置的变量:形参数
# def yue(num):
#     print("数字1")
#     print("数字2")
#     print("数字%s" % num)
#     print("数字4")
#     print("数字5")
# # 在函数调用的地方给的具体的值: 实参
# yue(6)
# a = 6
# yue(a)

# 吃
# # 位置参数，当函数的参数很多的时候必须要记住每一个位置是什么.
# def chi(good_food, no_good_food, drink, ice_cream):
#     print("今天吃 %s %s %s %s" %(good_food,no_good_food,drink,ice_cream))
# # 位置参数
# chi("豆浆", "炒粉", "奶茶", "冰淇淋")
# # 关键字参数
# chi(drink="白开水",ice_cream="冰",good_food="炒饭",no_good_food="空气")
# # 混合参数 位置参数先放前面,关键字在后面。
# chi("白饭","没有吃",ice_cream="冰棒",drink="营养快线")

# def regist(name,phone,gender):
#     print(name,phone,gender)
# regist("阿凡达","10010","男")
# regist("阿凡题","10086","男")
# regist("阿甘","10000","男")
# regist("女武神","11100","女")

# 如果一个位置参数出现多次,可以设置参数的默认值.
# 默认值参数必须放在后面
def regist(name,phone,gender="男"):
    print(name,phone,gender)
regist("阿凡达","10010")
regist("阿凡题","10086")
regist("阿甘","10000")
regist("女武神","11100","女")