# author azure

# 递归函数, 函数自己调用自己
# count = 1
# def func():
#     global count
#     print("哈喽",count)
#     count = count +1
#     func()
# func()
# 递归深度(maximum recursion depth) 你可以调用自己的次数，
# 官方文档中递归最大深度是1000, 在这之前就会给你报错误。


# # 遍历文件夹,打印出所有的文件和普通文件的文件名
# import os
# def func(filepath,n):
#     files=os.listdir(filepath) #查看当前目录中的文件
#     for file in files:  # 获取到每一个文件名
#         # 获取文件的路径
#         file_p = os.path.join(filepath,file)
#         if os.path.isdir(file_p): # 判断file_p是否为文件夹
#             print("\t"*n,"|-",file,":")
#             func(file_p,n+1)
#         else:
#             print("\t"*n,"--",file)
#     pass
# func("E:\文件库\K8S",0)

# 调整深度
import sys
print(sys.getrecursionlimit())

