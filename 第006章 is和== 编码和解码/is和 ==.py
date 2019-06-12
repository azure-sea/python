# author azure
# == 比较 比较的是值

# 字符串
# a = 'alex'
# b = 'alex'
# c = ' alex'
# print(a == b)  #输出True
# print(a == c)  #输出False

# 数值
# n = 10
# n1 = 10
# print(n == n1)  #输出True

#列表
# li1 = [1,2,3]
# li2 = [1,2,3]
# print(li1==li2)  #输出True

# is 是 比较 比较的是内存地址
#
# a = 'alex'
# print(id(a)) # 10461600 内存地址

# n = 10
# print(id(n)) # 71767872

# li = [1,2,3]
# print(id(li)) #19609040

#字符串
# a = 'alex'
# b = 'alex'
# print(a is b) #输出True

#数字
# n = 10
# n1 = 10
# print(n is n1) #输出True

# ---------------------------------------
# 小数据池

    # 数字   -5 ~ 256
    # 字符串中如果有特殊字符他们的内存地址就不一样
    # 字符串中单个*20以内他们的内存地址一样,单个*21以上内存地址不一致.

# a = 'a'*20
# b= 'a'* 20
# c= 'c'*21
# d= 'c'*21
# print(a is b)
# print(c is d)
# n = -8
# n1 = -8
# print(n is n1)

#列表
# li = [1,2,3]
# li2 = [1,2,3]
# print(li is li2)  #输出False

#元组
# tu =(1,2,3)
# tu1 =(1,2,3)
# print(tu is tu1) #输出False   #应pycharm的问题输出True

# 字典
# dic1 = {'name':'alex'}
# dic2 = {'name':'alex'}
# print(dic1 is dic2)   #输出False

# 总结:

    # == 比较 比较的两边的值
    # is 比较 比较的是内存地址 id()

