# author azure
# 1. 写代码,如有下列表,按照要求实现每一个功能
# li = ["alex","WuSir","ritian","barry","wenzhow"]
# 1)计算列表的长度并输出
# 2)列表中追加元素"seven",并输出添加后的列表
# 3)请在列表的第一个位置插入元素"Tony",并输出添加后的列表
# 4)请修改列表第二个位置插入元素"Kelly",并输出修改后的列表
# 5)请将列表L2 = [1,"a",3,4,"heart"]的每个元素添加到列表li中,一行代码实现,不允许循环添加.
# 6)请将字符串s = "qwert"的每一个元素添加到列表li中,一行代码实现,不允许循环添加.
# 7)请上传列表中的元素"eric",并输出添加后的列表
# 8) 请删除列表的第2个元素,并输出删除的元素和删除元素后的列表
# 9) 请删除列表中第2至4个元素,并输出删除元素后的列表
# 10) 请将列表所得元素反转,并输出反转后列表.
# 11) 请计算出"alex"元素在列表li里出现的次数,并输出该次数
li = ["alex","WuSir","ritian","barry","wenzhow"]
#1
print(len(li))
#2
li = ["alex","WuSir","ritian","barry","wenzhow"]
li.append("seven")
print(li)
#3
li = ["alex","WuSir","ritian","barry","wenzhow"]
li.insert(0,"Tony")
print(li)
#4
li = ["alex","WuSir","ritian","barry","wenzhow"]
li[1]="Kelly"
print(li)
#5
li = ["alex","WuSir","ritian","barry","wenzhow"]
l2 = [1,"a",3,4,"heart"]
li.append(l2)
print(li)
#6
li = ["alex","WuSir","ritian","barry","wenzhow"]
s ="qwert"
li.extend(s)
print(li)

#7
li = ["alex","WuSir","ritian","barry","wenzhow"]
li.append("eric")
print(li)

#8
li = ["alex","WuSir","ritian","barry","wenzhow"]
l2 = li.pop(2)
# li.remove("ritian")
print(l2)
print(li)

#9
li = ["alex","WuSir","ritian","barry","wenzhow"]
del li[2:4]
print(li)

#10
li = ["alex","WuSir","ritian","barry","wenzhow"]
li.reverse()
print(li)

#11
#
li = ["alex","WuSir","ritian","barry","wenzhow"]
count = 0
for i in li:
    if i == 'alex':
        count= count +1
    print(i)
print(count)


#2 写代码,有如下列表,利用切片实现每个功能
# li = [1,3,2,"a",4,"b",5,"c"]
# 1) 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
# 2) 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
# 3) 通过对li列表的切片形成新的列表l3,l3 = [1,2,4,5]
# 4) 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
# 5) 通过对li列表的切片形成新的列表l5,l5 = ["c"]
# 6) 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]

#1)
li = [1,3,2,"a",4,"b",5,"c"]
l1 = li[:3]
print(l1)

#2)
li = [1,3,2,"a",4,"b",5,"c"]
l2 = li[3:6]
print(l2)
#3)
li = [1,3,2,"a",4,"b",5,"c"]
l3 = li[::2]
print(l3)

#4)
li = [1,3,2,"a",4,"b",5,"c"]
l4 = li[1:6:2]
print(l4)

#5)
li = [1,3,2,"a",4,"b",5,"c"]
l5 = li[-1:-2:-1]
print(l5)

#6)
li = [1,3,2,"a",4,"b",5,"c"]
l6 = li[-3:-8:-2]
print(l6)

#3 写代码,如果有如下列表,按照要求实现每一个功能.
# lis = [2,3,"k",["qwe",20,["k1",["tt",3,"1"]],89],"ab","abv"]
# 1) 将列表lis中的"tt"变成大写(用俩种方式).
# 2) 将列表lis中的数字3变成字符串"100"(用俩种方式).
# 3) 将列表lis中的字符串"1"变成数字101(用俩种方式).

#1)
lis = [2,3,"k",["qwe",20,["k1",["tt",3,"1"]],89],"ab","abv"]
lis[3][2][1][0] = lis[3][2][1][0].upper()
print(lis)
# lis[3][2][1][0] ="TT"
# print(lis
#2)
lis = [2,3,"k",["qwe",20,["k1",["tt",3,"1"]],89],"ab","abv"]
lis[3][2][1][1] = '100'
print(lis)

# lis[3][2][1][1]= str(lis[3][2][1][1] + 97)
# print(lis)

#3)
lis = [2,3,"k",["qwe",20,["k1",["tt",3,"1"]],89],"ab","abv"]
lis[3][2][1][2] = '101'
print(lis)
# lis[3][2][1][2]= int(lis[3][2][1][2]) +100
# print(lis)

#4 请用代码实现:
# li = ["alex","eric","rain"]
# 利用下划线将列表的每个元素拼接成字符串"alex_eric_rain"

li = ["alex","eric","rain"]
s = ""
for i in li:
    s = s+i+"_" #alexericrain
print(s[:-1])

#5 利用for循环和range打印出下面列表的索引.
# li = ["alex","wusir",'abc',"cdv","wz"]
li = ["alex","wusir",'abc',"cdv","wz"]
for i in range(len(li)):
    print(i)

#6 利⽤for循环和range找出100以内所有的偶数并将这些偶数插⼊到⼀个新列表中
li=[]
for i in range(101):
    if i % 2 == 0:
        li.append(i)
print(li)

#7 利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
li=[]
for i in range(51):
    if i %3 ==0:
        li.append(i)
print(li)
#方式二
lst =[]
for i in range(0,50,3):
    lst.append(i)
print(lst)
#方式三
lis=[]
index =1
while index < 50:
    if index %3==0:
        lis.append(index)
    index +=1
print(lis)

#8 利⽤for循环和range从100~1，倒序打印。
lis = []
for i in range(100,0,-1):
    lis.append(i)
print(lis)

#9 利用for循环和range从100~10，倒序将所有的偶数添加到⼀个新列表中，
#  然后对列表的元素进⾏筛选，将能被4整除的数留下来。
lis = []
for i in range(100,10,-2):
    if i %4 ==0:
        lis.append(i)
print(lis)

#10 利用for循环和range，将1-30的数字⼀次添加到⼀个列表中，并循环这个
#   列表，将能被3整除的数改成*。
lis = []
index =0
for i in range(30):
    lis.append(i)
for i in lis :
    if i % 3 ==0:
        lis[index] ="*"
    index +=1
print(lis)
#方式二
# while index <len(lis):
#     if index %3 ==0:
#         lis[index] ="*"
#     index+=1
# print(lis)

#11 查找列表li中的元素，移除每个元素的空格，
#   并找出以"A"或者"a"开头，并 以"c"结尾的所有元素，
#   并添加到一个新列表中,最后循环打印这个新列表。
li = ["TaiBai ", "ale xC", "AbC ", "egon", " ri TiAn", "WuSir", " aqc"]
lis=[]
for i in li :
    if (i.strip()[0]=="a" or i.strip()[0]=="A" )and i.strip()[-1] =="c":
        lis.append(i)
for i in lis :
    print(i)
# 12，开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表 li = ["苍老师", "东京热", "武藤兰","波多野结衣"]
# 则将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换***），
# 并添加到这个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
'''
li  =["苍老师","东京热","武藤兰","波多野结衣"]
lst = []   # 定义一个列表
content = input("请输入评论:")  # 让用户输入
for el in li:   # 通过循环拿到列表中的每一个元素
    if el in content :  # 判断列表中都 元素有没有在输入的内容里面
        content =content.replace(el,"*"*len(el))
        # 如果有替换掉
# 把评论的信息追加到列表中
lst.append(content)
print(lst)
'''
#13 有如下列表
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# 我想要的结果是：
# "alex"
# 7,
# "taibai"
# ritian
li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
for i in li :
    if type(i) ==list :
        for el in i :
            print(el)
    else:
        print(i)
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# for i in range(len(li)):
#     if type(li[i])==list:
#         for h in range(len(li[i])):
#             print(li[i][h])
#     else:
#         print(li[i])
#14  把班级学生数学考试成绩录入到一个列表中:并求平均值.
#    要求: 录入的时候要带着姓名录入, 例如: 张三_44
'''
li = []
while 1:
    str_input = input('请输入您的姓名和分数(例如:张三_44),输入Q退出:')
    if str_input.lower() =='q':
        break
    else:
        ret = str_input.split('_')
        li.append(ret[1])
sum_num = 0
for i in li:
    sum_num = sum_num + int(i)
print(sum_num / len(li))
'''

#15 给出一个任意的数字n,从0开始数,数到n结束,把每个数字都房子列表中,在数的过程中出现7或者7的倍数,则向列表中添加一个"咣"
#   例如,输入10
# lst =[1,2,3,4,5,6,"咣",8,9,10]
lst =[]
for i in range(1,100):
    if i%7 ==0 :
        i =str(i).replace(str(i),"咣")
    lst.append(i)
print(lst)
