# author azure
# # 方式一：
# lst = []
# with open("实例模板",mode="r",encoding="utf-8") as f:
#     first = f.readline().strip().split(",")
#     for line in f:
#         dic = {} # 每一行一个字典
#         # 1,alex,10086,特斯拉
#         ls = line.strip().split(",")
#         dic['id'] = ls[0]
#         dic['name'] = ls[1]
#         dic['phone'] = ls[2]
#         dic['car'] = ls[3]
#        # print(dic)
#         lst.append(dic)
# print(lst)


# # 方式二
lst = []
with open("实例模板",mode="r",encoding="utf-8") as f:
    first = f.readline().strip().split(",")
    for line in f:
        dic = {} # 每一行一个字典
        # 1,alex,10086,特斯拉
        ls = line.strip().split(",")
        for i in range(len(first)):
            dic[first[i]]= ls[i]
       # print(dic)
        lst.append(dic)
print(lst)


