# author azure


# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# # 三角
# n = 6
# for i in range(1,n+1):
#     for k in range(2*n-2*i):
#         print("",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print()

lst = ["万五","张三","李四","腕儿"]

# for el in lst:
#     print(el)  # 没有索引
#
# for i in range(len(lst)):
#     print(i)
#     print(lst[i])

# 枚举
for index,el in enumerate(lst):
# for index,el in enumerate(lst,100): #从100开始
    print(index)
    print(el)