# author azure

# lst = [16, 18, 32, 54, 12, 9]
# lst.sort()  # list的方法(排序)
# print(lst)c

# # 内置函数中提供的一个统用的排序方案，sorted()
# s = sorted(lst)
# print(s)

#        2       3           4       3        3       2       2
# lst = ["聊斋","西游记","三国演义","葫芦娃","水浒传","年轮","亮剑"]
# def func(s):
#     return len(s)
#     # return len(s)%2
# ll=sorted(lst,key=func)
# ln=sorted(lst,key=func, reverse=True)   # 反排序
# print(ll)
# print(ln)

# key：排序方案, sorted 函数内部会把可迭代对象中的每个元素拿出来交给后面的key
#      后面的key计算出一个数字. 作为当前这个元素的权重。



# lst = [
# #     {'name':"汪峰","age":48},
# #     {'name':"章子怡","age":38},
# #     {'name':"alex","age":39},
# #     {'name':"azure","age":22},
# #     {'name':"sky","age":28}
# #     ]
# # # 方式一：
# # # def func(el):
# # #     return el['age']
# # # ll = sorted(lst,key=func)
# # # 方式二：
# # ll = sorted(lst,key=lambda el:el['age'])
# # print(ll)
