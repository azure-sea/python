# author azure
#  map()
#  映射函数
#  语法: map(function, iterable) 可以对可迭代对象中的每⼀个元素进⾏映射. 分别取执⾏function

lst = [1,4,7,2,5,8]
# 计算列表中每个数字的平方
# # 方式一:
# for el in lst:
#     print(el**2)

# # 方式二:
# ll = []
# for el in lst:
#     ll.append(el**2)
# print(ll)

# # 方式三:
# def func(el):
#     return el**2
# m = map(func,lst)  # 把后面的可迭代对象中的每个元素传递给function函数, 结果就是function的返回值
# print("__iter__" in dir(m))
# print(list(m))

# 分而治之
# map(func1,map(func2,map(func3,lst)))

# #  返回二个列表的和
# lst1 = [1,3,5,7,9,100]
# lst2 = [2,4,6,8,10]
# # 也存在水桶效应,zip()
# m = map(lambda x,y: x+y,lst1,lst2)
# print(list(m))

