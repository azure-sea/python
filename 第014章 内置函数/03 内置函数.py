# author azure

# lst = ["白蛇传","西游记","三国演义"]
# # it = lst.__iter__()
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
# it = iter(lst)  # 内部封装的是__iter__()
# print(it.__next__())
# print(next(it)) # 内部封装的是__next__()

# print(bin(5)) # 5的二进制。
# print(oct(8)) # 0o 八进制
# print(hex(16)) # 0x十六进制

# print(abs(-8)) # 求绝对值(取模)
# print(divmod(10,2)) # 计算商和余数
# print(round(5.6))     # 四舍五入
# print(pow(2,3,3))       # 求次幂(a的b次幂) 第三个参数，计算余数
# print(sum([1,2,3,5],3))         # 求和
# print(min([5,12,35,1]))       # 最小值
# print(max([5,12,35,1]))       # 最大值

# lst= ["马化腾","马云","马超"]
#
# ll = reversed(lst)
# print(ll)

# lst= ["马化腾","马云","马超"]
# s= slice(1,3,2) #切片
# print(lst[s])
# print(lst[1:3:2])

# s = "你好, world"
# print(memoryview(s.encode("utf-8")))

# print(ord("a")) # 查看字母a在编码表的位置
# print(ord("A"))
# print(ord("中")) # 20013
# print(chr(20013)) # 通过编码位置找到文字。
# print(chr(20013))

# print(ascii("a"))
# print(ascii("中")) #\u

# # 周杰伦说:"昆凌特别美"
# print('周杰伦说:''"昆凌特别美"')
# print("周杰伦说:\"昆凌特别美\"")

# # 字符串
# print(format('test', '<20')) # 左对⻬
# print(format('test', '>20')) # 右对⻬
# print(format('test', '^20')) # 居中
# # 数值
# print(format(3, 'b')) # ⼆进制
# print(format(97, 'c')) # 转换成unicode字符
# print(format(11, 'd')) # ⼗进制
# print(format(11, 'o')) # ⼋进制
# print(format(11, 'x')) # ⼗六进制(⼩写字⺟)
# print(format(11, 'X')) # ⼗六进制(⼤写字⺟)
# print(format(11, 'n')) # 和d⼀样
# print(format(11)) # 和d⼀样
# # 浮点数
# print(format(123456789, 'e')) # 科学计数法. 默认保留6位⼩数
# print(format(123456789, '0.2e')) # 科学计数法. 保留2位⼩数(⼩写)
# print(format(123456789, '0.2E')) # 科学计数法. 保留2位⼩数(⼤写)
# print(format(1.23456789, 'f')) # ⼩数点计数法. 保留6位⼩数
# print(format(1.23456789, '0.2f')) # ⼩数点计数法. 保留2位⼩数
# print(format(1.23456789, '0.10f')) # ⼩数点计数法. 保留10位⼩数
# print(format(1.23456789e+10000, 'F')) # ⼩数点计数法.


# s = {"爱情公寓","绝技","妖猫传","煎饼侠","郭德纲"}
# s.add("空天猎") # 可变，不可哈希
# print(s)
# print(hash(s))  # 可变

# s = frozenset({"战狼2","我不是药神","西虹市首富","捉妖记"})  # 不可变的列表
# print(hash(s)) # 可哈希,不可变。
#
# lst = ["张国荣","黄渤","郭达森","泰森","甄子丹"]

# for el in lst:
#     print(el)
#
# for i in range(len(lst)):
#     print(i,lst[i])

# for i,el in enumerate(lst):
#     print(i,el)

# # all() and 并
# print(all([True,1,1,1]))
# # any() or 或
# print(any([True,0,1,1]))
# 所有的空,都是False

# # zip()
# lst1 = ["甜蜜蜜","往事只能回味","难忘今宵","粉红的回忆","十年"]
# lst2 = ["邓丽君","韩宝仪","李谷一","王宝强"]
# lst3 = ["2000","3000","50","1200"]
# a = zip(lst1,lst2,lst3) # 水桶效应
# print("__iter__"in dir(a)) # 可迭代的
# for el in a:
#     print(el)

# s = "5 + 6"
# ret = eval(s) # 动态执行一个代码片段,重点在返回
# print(ret)

# a = "{'name':'汪峰','age':'58', 'wife':{'name':'国际章','age':'38'}}" # json。像字典一样的东西
# d = eval(a) # 还原回字典,列表
# print(d['name'])

# s = 'a = 10'
# exec(s) # 执行代码
# print(a) # pycharn 报错不一定是对的

# content = input("请输入代码:")
# exec(content)
# print(a)



# class Employee:
#     empCount=0
#
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#
#     def displayEmployee(self):
#         print("Name：",self.name,",Salary:",self.salary)
# emp1 = Employee("Zare",2000)
# print(emp1)
# emp1.displayEmployee()
#
# for letter in  'Python':
#     print(letter)
# print("Total Employee %d" % Employee.empCount)


# 参考资料:
# https://www.processon.com/view/link/5b4ee15be4b0edb750de96ac
