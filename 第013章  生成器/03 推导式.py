# author azure

# lst = []
# for i in range(1,16):
#     lst.append("pyrhon"+str(i))
# print(lst)

# # 推导式：用一句话生成一个列表
# # lst = ["python"+str(i) for i in range(1,16)]
# # print(lst)
# 语法：[结果 for循环 判断]

# lst = [i for  i in  range(100) if i%2 == 1]
# print(lst)

# # 100 以内能被3整除的数的平方
# lst = [i*i for i in range(100) if i%3==0]
# print(lst)

# # 寻找名字中带有二个e的人名
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven','Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# 正常取值
# for line in names:
#     for name in line:
#         if name.count("e") == 2:
#             print(name)

# lst = [name for line in names for name in line if name.count("e") == 2]
# print(lst)


# # [11,22,33,44] => {0:11,1:22,2:33,3:44}
# lst = [11,22,33,44]
# dic = {i:lst[i] for i in range(len(lst))}
# print(dic)

# 语法:{k:v for循环 条件筛选}
#
# dic = {"jj":"林俊杰","ll":"周杰伦","mm":"小莫","zs":"赵四",}
# d = {v:k for k,v in dic.items()}
# print(d)

# s = {i for i in range(100)} # 可去重
# print(s)

# lst = [1,2,3,4,4,2,7,6,1,1]
# # s = set(lst) # 通过集合去重
# # print(s)
# s = {el for el in lst}
# print(s)