# author azure
# 闭包 特点:在内层函数中访问外层函数的变量
# 闭包的作用:
#        1.可以保护你的变量不受侵害
#        2. 可以让一个变量常住内存
# a = 10  # 不安全的
# def outher():
#     global a
#     a = 20
#
# def outher_2():
#     global a
#     a = 30
#
# outher()
# outher_2()
# print(a)

# def outher():
#     a = 10   # 对外届不开放的
#     def inner():
#         nonlocal a
#         a = 20
#         print(a)
#     inner()
# def outer():
#     a = 10   # 常驻内存，为了inner执行的时候有值。
#     def inner():
#         print(a)  #
#     return inner
#
# fn = outer()
# print(".....")
# fn()  # 调用的时机是不定的。

# 简单爬虫
# from urllib.request import urlopen
#
# urlopen("http://www.baidu.com").read()
