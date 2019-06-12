# author azure
name = "aleX leNb"
print(name.strip()) #移除name对应的值两边的空格,并输出处理结果.
print(name.lstrip("al"))#移除name变量左边的"al"并输出处理结果.
print(name.rstrip("Nb"))#右边的"Nb".并输出处理结果.
print(name.strip("a").strip("b")) #移除name变量开头的"a"与最后的"b",并输出结果.
print(name.startswith("al"))# 判断name变量是否已"al"开头,并输出结果.
print(name.endswith("Nb"))# 判断name变量是否已"Nb"结尾,并输出结果.
print(name.replace("l","p")) #将name变量对应的值中所有的"l"替换成"p",并输出结果.
print(name.replace("l","p",1))#将name变量对应的值中第一个的"l"替换成"p",并输出结果.
print(name.split("l")) #将name变量对应的值根据 所有的"l"分割,并输出结果.
print(name.split("l",1))#将name变量对应的值根据 第一个"l"分割,并输出结果.
print(name.upper()) #将name变量对应的值变成大写,并输出结果.
print(name.lower()) #将name变量对应的值变成小写,并输出结果.
print(name.capitalize()) #将name变量对应的首字母"a"大写,并输出结果
print(name.count("l")) #判断name变量对应的值字母"l"重出现的次数,并输出结果
print(name.count("l",4)) # 判断name变量对应的值前4位字母"l"重出现的次数,并输出结果
print(name.index("N")) #从name变量对应的值中找到"N"对应的索引(如果找不到则报错),并输出结果
print(name.find("N")) #从name变量对应的值中找到"N"对应的索引(如果找不到则返回-1),并输出结果
print(name.index("X le")) #从name变量对应的值中找到"X le"对应的索引,并输出结果.
print(name[1]) #请输出name变量对应的值的第2个字符
print(name[:3]) #请输出name变量对应的值的前3个字符
print(name[-2:])#请输出name变量对应的值的后2个字符
#请输出name变量对应的值中"e"所在索引位置.
index = 0  #手动记录
for c in name:
    if c=="e":
        print(index)
    index = index +1

s = "123a4b5c"
print(s[:3]) #1) 通过对S切片形成新的字符串s1, s1 = "123"
print(s[3:6]) #2) 通过对S切片形成新的字符串s2, s2 = "a4b"
print(s[::2]) #3) 通过对S切片形成新的字符串s3, s3 = "1345"
print(s[1:7:2])  #4) 通过对S切片形成新的字符串s4, s4 = "2ab"
print(s[-1])  #5) 通过对S切片形成新的字符串s5, s5 = "c"
print(s[-3::-2]) #6) 通过对S切片形成新的字符串s6, s6 = "ba2"

#3.使用while和for循环分别打印字符串a="asdfer"中每个字符.
a="asdfer"
index = 0
while True:
    print(a[index])
    index+=1
    if index == len(a):
        break
#---------方式二-------#
for i in  a:
    print(i)
########################
#4使用for循环对b="asdfer"进行循环,但是每次打印的内容都是"asdfer"
b="asdfer"
count = 0
for i in b:
    print(b)
    count +=1
    if count == 3:
        break
#5使用for循环对c="abcdefg"进行循环,每次打印的内容是每个字符加上sb,
c="abcdefg"
for i in c:
    print(i+"sb")
#6使用for循环对s="321"进行循环,打印的内容依次是:"倒计时3秒","倒计时2秒","倒计时1秒","出发".
d = "321"
for i in d:
    print("倒计时%s秒" % (i))
else:
    print("出发")
#7 实现一个整数加法计算器(两个数相加):
#  如: count = input("请输入内容:")用户输入: 5+9或5+ 9 ,然后进行分割在进行计算.
'''
shizi = input("请输入内容:")
# 处理空格
shizi= shizi.replace(" ","")
lst = shizi.split("+")
print(int(lst[0])+ int(lst[1]))
'''
#8计算机用户输入内容有几个整数(以个数为单位).
'''
zhengshu = 0
content = input("请输入内容: ")
for c in content:
    if c.isdigit():
        zhengshu = zhengshu + 1
print(zhengshu)
'''
#9 写代码,完成下列需求:
#   用户可持续输入(使用while循环),用户使用情况:
#   输入A,则显示走大路回家,然后在让用户进一步选择:
#        是选择公交车,还是步行?
#         选择公交车,显示10分钟到家,并退出整个程序
#         选择步行,显示20分钟到家,并退出
#    输入B,则显示走小路回家,并退出
#    输入C,则显示绕道回家,然后在让用户进一步选择:
#         选择A区,还是B区
#         选择A区,显示一个半小时回家,,并让其重新输入ABC选项目
#         选择B区,显示二个小时到家,并让其重新输入ABC选项目
'''
while 1:
    count = input("请选择路线A,B,C:")
    if count == 'A':
        print("走大路回家")
        traffic=input("请选择公交还是步行?")
        if traffic =='公交':
            print("10分钟")
        elif traffic == '步行':
            print("20分钟")
        else:
            print("死亡")
        break
    elif count == 'B':
        print("小路")
        break
    elif count == 'C':
        print("绕道")
        traffic2 = input("请选择A区还是B区?")
        if traffic2 == 'A区':
            print("一个半")
            break
        elif traffic2 == 'B区':
            print("二小时")
            continue
        else:
            print("尚方宝剑")
    else:
        print("error")
'''
#判断输入的内容\
content = input("输入:")
daxie = 0
xiaoxie = 0
shuzi = 0
other = 0
for c in content:
    if c.isupper():
        daxie +=1
    elif c.islower():
        xiaoxie +=1
    elif c.isdigit():
        shuzi +=1
    else:
        other +=1

print(daxie,xiaoxie,shuzi,other)
