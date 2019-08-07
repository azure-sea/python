# author azure

# a = 10
# b = a # 赋值操作
# print(b)

# def func():
#     print("我是一个函数")
# func()
def func1():
    print("1")
def func2():
    print("1")
def func3():
    print("1")
# lst = [func1(), func2(),func3()]
# for el in lst:
#     el

# lst = [func1, func2,func3]
# for el in lst:
#     el()
# 函数名的变量名

# 函数名可以作为参数传递给函数
# def my():
#     print("this my")
# def proxy(fn):  # 代理模式, 装饰器
#     print("在处理前面")
#     fn()
#     print("在处理后面")
# proxy(my)  把函数名作为参数传递给另一个参数

#
# def func1():
#     print("this is func1")
# def func2():
#     print("this is func2")
#
# def func(fn,gn): # 函数名可以作为参数传递。
#     print("this is func")
#     fn()
#     gn()
#     print("stop .....")
# func(func1,func2)

# def func():
#     print("this is func")
#     a = 10
#     def inner():
#         print("this is inner")
#     return  inner
# # ret = func()
# # ret()
# func()()  # 写运行func() 然后在返回值上加()



