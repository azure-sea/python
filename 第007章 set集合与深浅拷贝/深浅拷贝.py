# author azure

lst1 = ["⾦⽑狮王", "紫衫⻰王", "⽩眉鹰王", "⻘翼蝠王"]
# lst2 = lst1   # 浅拷贝 (复制内存地址)
# lst2 = lst1.copy() #浅拷贝
lst2 = lst1[:]  # 通过切片产生新列表.
lst1.append("杨逍")


print(lst1)
print(lst2)

