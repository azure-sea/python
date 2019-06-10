# author azure

#带w的。只要操作，就会清空源文件
# 如果文件不存在，会自动创建文件。
# f = open("写文件测试",mode="w",encoding="UTF-8")
# f.write("测试写》》》》OK\n")
# f.write("写成功了\n")
# f.flush()
# f.close()

# 文件操作 a 模式(追加)
# f = open("写文件测试",mode="a",encoding="UTF-8")
# f.write("a模式测试\n")
# f.write("a模式测试成功\n")
# f.flush()
# f.close()


# 文件操作 b 模式，需要和其他r w a 一起组合。b(bytes) 处理为 非文本文件。
# f = open("蜂鸟.jpg",mode="rb") # 因为带b 使用无法使用encoding
# e = open("新蜂鸟.jpg",mode="wb")
# for line in f: #读取数据。line不知道读取多少数据.
#     e.write(line)
# f.close()
# e.flush()
# e.close()

