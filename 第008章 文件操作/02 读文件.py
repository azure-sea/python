# author azure

# 文件路径:
#    1. 绝对路径，从磁盘的根目录寻找，或者 从互联网上寻找一个路径。
#    2. 相对路径，相对当前程序所在的位置。
# of = open("E:\\test\第8章 文件操作\读文件测试.txt",mode="r",encoding="UTF-8")

# of = open("读文件测试.txt",mode="r",encoding="UTF-8") #记事本用gbk
# s = of.read()
# print(s)
# of.close()

# 1 大文件或日志读取方法一：
# f = open("床前明月光",mode="r",encoding="UTF-8")
# s = f.readline().strip() # 一次读一行  strip 去除左右空白
# print(s)   # 打印默认格式为 print(s,end="\n")
# s = f.readline().strip() # 一次读一行
# print(s)
# s = f.readline().strip() # 一次读一行
# print(s)
# s = f.readline().strip() # 一次读一行
# print(s)
# f.close()

# 2 大文件或日志读取方法二：
# f = open("床前明月光",mode="r",encoding="UTF-8")
# while 1:
#     s = f.readline().strip()
#     if s!="":
#         print("内容是:",s)   #程序一直运行，内存无法得到释放。
# f.close()

# 3 大文件或日志读取方法三：
# f = open("床前明月光",mode="r",encoding="UTF-8")
# for line in f:  #文件是一个可迭代对象
#     print(line.strip()) #一行一行的处理数据
# f.close()