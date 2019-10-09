# author azure

# 取随机模块

import random

# # 取随机小数：科学计算
# print(random.random()) # 取0-1之间的小数
# print(random.uniform(10,200))  #取10-200之间的小数

# # 取随机整数：彩票 抽奖
# print(random.randint(1,2))   # [1,2]
# print(random.randrange(1,2))  # [1,2)
# print(random.randrange(1,200,2))  # 取奇数

# # 从一个列表中随机抽取值
# l = ['a','b',1,2,3]
# print(random.choice(l))    # 随机从列表中取一个值
# print(random.sample(l,2))  # 随机从列表中取 N 个值

# # 打乱一个列表的顺序, 在原列表的基础上直接进行修改, 节省空间。
#  洗牌
# l = ['a','b',1,2,3]
# random.shuffle(l)
# print(l)

# 验证码
   # 4位数字验证码
   # 6位数字验证码
   # 6位数字+字母验证码

# # 4位数字验证码
# s = ''
# for i in range(4):
#     sum = random.randint(0,9)
#     s += str(sum)
# print(s)

# # 函数版本
# def code(n=6):
#     s = ''
#     for i in range(n):
#         sum = random.randint(0, 9)
#         s += str(sum)
#     return s
# print(code(4))
# print(code())

# 6位数字+字母验证码
# s = ''
# for i in range(6):
#     # 生成随机的大写字母,小写字母,数字各一个
#     num = str(random.randint(0,9))
#     alpha_upper = chr(random.randint(65,90))
#     alpha_lower = chr(random.randint(97,122))
#     res = random.choice([num,alpha_upper,alpha_lower])
#     s += res
# print(s)

# # 函数版本
# def code(n = 6):
#     s = ''
#     for i in range(n):
#         # 生成随机的大写字母,小写字母,数字各一个
#         num = str(random.randint(0,9))
#         alpha_upper = chr(random.randint(65,90))
#         alpha_lower = chr(random.randint(97,122))
#         res = random.choice([num,alpha_upper,alpha_lower])
#         s += res
#     return s
# print(code(4))
# print(code())

# 进阶版
# def code(n = 6,alpha = True):
#     s = ''
#     for i in range(n):
#         num = str(random.randint(0,9))
#         if alpha:
#             alpha_upper = chr(random.randint(65,90))
#             alpha_lower = chr(random.randint(97,122))
#             num = random.choice([num,alpha_upper,alpha_lower])
#         s += num
#     return s
# print(code(4,False))
# print(code(alpha=False))

# 发红包
    # 红包数量 钱数
    # 拼手气红包
