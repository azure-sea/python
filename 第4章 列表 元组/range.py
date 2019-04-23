# author azure
# range() 是一个可迭代对象
# 1. range(n) 0 -> n-1
for i in range(5):
    print(i)
# 2. range(m,n) m -> n-1
for i in range(4,7):
    print(i)
# 3. range(m,n,q) m -> n-1 每q个取1个
for i in range(1,10,3):
    print(i)

for i in range(100, 95, -1):
    print(i)
#        0      1        2        3      4
lst = ["砂锅","馒头","盖浇饭","刀削面","烤羊","煎饼"]
# for el in lst:
#     print(el)
# 获取到列表的索引, 拿到索引之后,就可以拿到元素.
for i in range(len(lst)):
    print(i)   # i 就是索引了
    print(lst[i])