# author azure

# 无论读取多少内容。光标在哪，写入的时候都是在结尾写入 #一开始就写入,写入在开头。
# r+读写同时存在的模式
# f = open("r+测试",mode="r+",encoding="utf-8")
# s = f.read()
# print(s)
# f.write("A+测试,测试成功") #在末尾写。
# f.close()

# 坑一
# f = open("r+测试",mode="r+",encoding="utf-8")
# f.write("葫芦娃")
# s= f.read()
# print(s)
# f.close()

# w+ 很少用。因为会清空文件内容
# f = open("w+测试",mode="w+",encoding="utf-8")
# f.write("w+测试是否成功？ 成功") # 写完以后光标在最后， 读取结果为空。
# f.seek(0) # 移动光标至开头
# s = f.read()
# print("读取内容为:",s)
# f.flush()
# f.close()

# a+

# f = open("a+测试",mode="a+",encoding="utf-8")
# f.write("A+写测试")
# f.seek(0)
# s =f.read()
# print(s)
# f.flush()
# f.close()