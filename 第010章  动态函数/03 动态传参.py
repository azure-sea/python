# author azure

# 非动态传参 无法确定参数数量多少。
# def chi(good_food, no_good_food, drink, ice_cream):
#     print(good_food, no_good_food, drink, ice_cream)
# chi("豆浆", "炒粉", "奶茶", "冰淇淋")

#  顺序： 位置参数=> * args(arguments)
# # * 在这里表示接收位置参数的动态传递参数，接收到的是元组
# def chi(*food): # 参数名为food  *表示动态传参
#     print(food)
# chi("豆浆", "炒粉", "奶茶", "冰淇淋")
# chi()   # 结果为: 空函数

# #  组合方式一:
# def chi(name,*food):
#     print(name+"要吃",food)
# chi("azure", "炒粉", "奶茶", "冰淇淋")

# 关键字的动态传参
# def chi(**food):
#     print(food)
#
# chi(good_food = "狗不理",no_good_food = "汉堡")

# 顺序
# 位置参数，*args, 默认值参数, **kwargs
# 以上参数可以任意搭配使用

# 1. 实参：
#        位置参数
#        关键字参数
#        混合参数(位置, 关键字)

# 2. 行参:
#        位置参数
#        默认值参数
#        动态传参:
#                 *args: 位置参数动态传参
#                 **kwargs: 关键字参数动态传参
#         顺序: 位置、*args、默认值、**kwargs.


# # def func(a,*args,**kwargs,c="哈哈"):   # 错误示例
# def func(a,*args,c="哈哈",**kwargs):
#     print(a,args,c,kwargs)
# func(1,2,3,d=5,c=6)

# 单行注释
'''多行注释'''

# 函数注释
# def func(a,b):
#     """
#     这个函数是用来计算a和b的和
#     :param a: 第一个数
#     :param b: 第二个数
#     :return:  返回的是两个数的和
#     """
#     return a+b
# print(func.__doc__)  # document文档

# 接收所有参数
# def func(*args,**kwargs):  # 无敌参数  *args 相当于聚合的作用
#     print(args,kwargs)
# func(1,2,3,4,5,a=6,b=7,c=8)


# # 形参: 聚合
# def func(*food):  # 聚合, 位置参数
#     print(food)
# lst = ["鸡蛋","煎饼果子","猪蹄","鸡"]
# func(lst)
# func(lst[0],lst[1],lst[2],lst[3])
# func(*lst)  # 打散, 把list、tuple、set、str 进行迭代打撒


# # 聚合成关键字参数
# def func(**kwargs):
#     print(kwargs)
# dic = {"name":"azure",'arg':'18'}
# func(name=dic['name'],arg= dic['arg'])
# func(**dic)  #  打散成关键字参数
