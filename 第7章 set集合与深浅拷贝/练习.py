# author azure

# a = 'azure'  # 这是第一次产生alex
# b = 'azure'  # 这句话不会产生新的字符串
#
# print(id(a), id(b))

# a = "谦虚"
# b = "谦虚"
# lst = ["jj",'jay',"谦虚"]
# lst2 = ["jj",'jay',"谦虚"]
#
# print(id(lst), id(lst2))

a = [1,2,3]
b = a
c = b

#列表的创建
print(c == a) # 判断的是值.
print(c is a) # 判断两个变量指向的是同一个对象

s = '中'
bs = s.encode("utf-8")
print(bs)