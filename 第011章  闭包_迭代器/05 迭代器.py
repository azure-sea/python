# author azure

# s = "你好啊"
# s = 123
# for i in s:
#     print(i)
# print(dir(str)) # dir 查看XX类型的数据可以执行哪些方法, __iter__ iterable
# print(dir(list))

# 所有的带__iter__ 可以所有for循环, 迭代对象，

# 可迭代对象可以使用__iter__()来获取到迭代器
# 迭代器里面有__next__()
# s = "你好"
# it = s.__iter__() # 获取迭代器
# print(dir(it))   # 迭代器里面有__iter__ 还有__next__
# # 1. 只能向前
# # 2. 几乎不占用内存,节省内存
# # 3. for 循环
# print(it.__next__())
# print(it.__next__())
# # print(it.__next__())


# 迭代器模拟for循环
# lst = ["张无忌","花荣","小鱼儿","花无缺","郭靖"]
# # for el in lst:  # 底层用的是迭代器
# #     print(el)
#
# it = lst.__iter__() # 获取迭代器
# while 1:
#     try:
#         el = it.__next__() # 获取下一个元素
#         print(el)
#     except StopIteration:   # 出现StopIteration问题except负责（处理错误）
#         break

# lst = ["张无忌为什么这么帅","我不信","你信吗？"]
# it = lst.__iter__()
# # print("__iter__" in dir(it))
# # print("__next__"in dir(it))
# # 可以通过dir来判断数据是否是可迭代的，以及数据是否是迭代器。
#
# 官方判断
# from collections.abc import Iterable   # 可迭代对象
# from collections.abc import  Iterator  # 迭代器
#
# print(isinstance(lst,Iterable))
# print(isinstance(lst,Iterator))
#
# print(isinstance(it,Iterable))
# print(isinstance(it,Iterator))

lst = ["万五","张三","李四","腕儿"]
it = lst.__iter__()
# print(it.__next__())

# list(参数)把参数进行循环迭代
s = list(it)  # 在list中,一定存在for,一定存在__next__()
print(s) # ["万五","张三","李四","腕儿"]
