# author azure
# print((1+3)*5)
# print((3))
# tu = (3)
# print(type(tu))
# ts = (3,) # 元组中如果只有一个元素.需要在括号里写一个","
# td = tuple() # 空元组
# print(type(ts))
# print(type(td))

# tu = ("人民币","美元","银币","欧元")
# #元组不能添加,删除,修改
# print(tu[2])
# print(tu[::2])
# for ln in tu:
#     print(ln)

# 元组的第一层是不允许进行赋值的,内部的子元素是可变,这取决与子元素是否是可变对象.
tu = (1,"哈喽","how are you",[])
tu[3].append("123")
print(tu)
