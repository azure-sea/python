# author azure

# num = input("请输入一个三位数:")
# # for c in num:
# #

#2.完成彩票36选7的功能 从36个数中随机的产生7个数,最终获取到7个不重复的数据作为最终的开奖结果.
# 提示 随机数:
# from random import randint
# randint(0,20) #0-20的随机数。

# from random import randint
# s = set()
# while len(s) < 7 :
#     r = randint(1, 36)
#     s.add(r)
# print(s)

# 3.税务部门征收所得税。规定如下:
#         1). 收入在2000以下的。免征.
#         1). 收入在2000-4000以下的，超过2000部分征收3%的税。
#         1). 收入在4000-6000以下的，超过4000部分征收5%的税。
#         1). 收入在6000-10000以下的，超过6000部分征收8%的税。
#         1). 收入在10000以上的，超过部分征收20%的税。
#    注，如果一个人的收入是8000，那么他要交2000到4000的税加上4000到6000的税务加上6000到8000的税。
#                   收入= 8000-（4000-2000）*3%-（6000-4000）*5%-（8000-6000）*8%
#        让用户输入它的工资，计算最后用户税后工资。
#
# salary = int(input("请输入你的工资:"))
# if salary <=2000:
#     print("没有税,税后%s " % salary)
# elif salary <=4000:
#     sw =(salary-2000)*0.03
#     print("共交税 %s 税后%s" % (sw,salary-sw))
# elif salary <=6000:
#     sw = 2000*0.03 +(salary-4000)*0.05
#     print("共交税 %s 税后%s" % (sw,salary-sw))
# elif salary <=10000:
#     sw = round(2000*0.03 +2000*0.05+(salary-6000)*0.08,2)
#     print("共交税 %s 税后%s" % (sw,salary-sw))
# elif salary >10000:
#     sw = round(2000*0.03 +2000*0.05+4000*0.08+(salary-10000)*0.2,2)
#     print("共交税 %s 税后%s" % (sw,salary-sw))


