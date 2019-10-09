# author azure
# 一：用列表推导式中下面小题
# # 1.过滤长度小于3的字符串列表，并将剩下的转换成大写字母。
# lst = ["caixukuang","wyf","wynZ","王宇","不认识"]
# ll = [name.upper() for name in lst if len(name) >3]
# print(ll)

# # 二: 求(x,y)其中0-5之间的偶数,y是0-5之间的奇数组成的元组列表[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]
# lst = [(i,n)for i in range(5) for n in range(5) if i%2==0 and n%2==1]
# print(lst)

# # 三：求M中 3,6,9组成的列表M=[[1,2,3],[4,5,6],[7,8,9]]
# M=[[1,2,3],[4,5,6],[7,8,9]]
# print([i[2] for i in M ])

# # 四: 求出50以内能被3整除的数的平方,并放到一个列表中。
# print( [i**2 for i in range(50) if i % 3 == 0] )

# # 五: 构建一个列表：[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6)]
# print([(i,i+1) for i in range(6)])

# # 六: 构建一个列表：[0,2,4,6,8,10,12,14,16,18]
# # print( [i for i in range(20) if i %2 == 0])

