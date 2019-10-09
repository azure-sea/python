# author azure
#
# def func():
#     print("你好")
#
# print(func)   # 内存地址 0x0038F7C8
# fn = func
# print(fn)     # 内存地址 0x0038F7C8
# func()
# fn()
#
# def gn(fc):
#     print(fc)  #<function func at 0x039EF7C8>
#     print(fc.__name__)   # func
#     fc()       # 等价于func()
#     pass
# gn(func)   #<function func at 0x039EF7C8>
