# author azure

# # 普通的正常函数
# def func(n):
#     return n*n
# ret = func(9)
# print(ret)
#
# # 匿名函数 语法 lambda 参数 : 返回值
# a = lambda n : n*n
# ret = a(9)
# print(ret)
#
# print(func.__name__) # 查看函数的名字
# print(a.__name__)    # 匿名函数的__name__值为<lambda> 函数的名字可以认为是“a”

fn = lambda *args: max(args) # 单行函数
print(fn(1,2,3,4,))