# author azure

# 三. filter()
#  筛选函数
#  语法: filter(function. Iterable)
#  function: 用来筛选的函数. 在filter中会自动的把iterable中的元素传递给function. 然后
# 根据function返回的True或者False来判断是否保留此项数据


# 通过filter筛选出姓张的过滤
# lst = ["张无忌","张一山","杨紫","鞠婧祎","李连杰","azure"]
# # def func(el):
# #     if el[0] == '张':
# #         return False # 不需要
# #     else:
# #         return True  # 需要的
#
# # f = filter(func,lst) # 将lst中每一项传递给func,所有返回True的都会保留,所有的返回False的被过滤
#
#
# # print("__iter__" in dir(f))  # 判断是否可以进行迭代
# # for e in f:
# #     print(e)
# # 方式二：
# l = filter(lambda el: el[0] !="张",lst)
# for e in l:
#     print(e)


# lst = [
#     {'name':"汪峰","score":79},
#     {'name':"章子怡","score":58},
#     {'name':"alex","score":96},
#     {'name':"azure","score":100},
#     {'name':"sky","score":28}
#     ]
# f = filter(lambda el:el['score'] > 60 ,lst) # 留下socre大于60的人
# print(list(f))


