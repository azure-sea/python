# author azure
# tu = (i for i in range(10)) # 没有元组推导式. 生成器表达式。
# print(tu)
# print(tu.__next__())
# print(tu.__next__())
# print(tu.__next__())
# print(tu.__next__())
# print(tu.__next__())

# lst = [i for i in range(10)] # 列表
# print(lst)
#
# gen = (i for i in range(10)) # 生成器, 惰性机制。
# print(gen.__next__())

# # 生成器函数
# def func():
#     print(111)
#     yield 222
# g = func() # 获取生成器
#
# g1 = (i for i in g) # 生成器
# g2 = (i for i in g1) # 生成器
# print(list(g))  # ??? [222] 源头，从源头把数据拿走了。
# print(list(g1)) # ??? []  这里执行的时候，源头已经没有数据了。
# print(list(g2)) # ??? []  这里也获取不到数据

# # 求和
# def add(a,b):
#     return a+b
# # 生成器函数 # 0-3
# def test():
#     for r_i in range(4):
#         yield r_i
# g = test() # 获取生成器
# for n in [2,10]:
#     g = (add(n, i) for i in g)
# # n=2
# # g= (add(n, i) for i in (add(n, i)for i in g))
# #
# # n=10
# # g= (add(n, i) for i in g)
#
# print(list(g))

