# author azure

# def func():
#     print("哈哈哈")
#     yield 1 # return和yield都可以返回数据
#     print("嘻嘻嘻")
# gen = func() #不会执行你的函数,拿到的是生成器
# # print(func())  # generator object 生成器对象
# ret = gen.__next__()   # 和执行写一个yield
# print(ret)
# gen.__next__()

# 函数中如果有yield
# yield：相当于return，可以返回数据，但是yeild不会彻底中断函数，分段执行函数


# # send() 和__next__()是一样的，可以执行到下一个yield,可以给上一个yield位置传值。
# def func():
#     print("一段")
#     yield 123
#     print("er")
#     yield 345
#     print("三段")
#     yield 567
#     print("尾部")
#
# g = func()
# # 没有上一个yield 所以不能使用send() 开头必须是__next__()
# print(g.__next__())   # 打印一段，返回123
# print(g.send("321"))


# def eat():
#     print("早餐吃什么")
#     a = yield "馒头"
#     print("a=",a)
#     b = yield "鸡蛋"
#     print("b=",b)
#     c = yield "白开水"
#     print("c=",c)
#     yield "over"
# gen = eat()     #获取生成器
#
# ret1 = gen.__next__()
# print(ret1) #馒头
#
# ret2 = gen.send("胡辣汤")
# print(ret2)

def func():
    yield 1
    yield 13
    yield 26
    yield 88
    yield 46
    yield 100

for i in func():  #for的内部一定有__next__()
    print(i)

print(list(func()))  #内部也有__next__()