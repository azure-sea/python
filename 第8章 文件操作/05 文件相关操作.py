# author azure

# f = open("床前明月光",mode="r",encoding="utf-8")
# for line in f:
#     print(line.strip())
# # 第二次for 循环没有读取数据。 因为光标在最后 通过seek移动光标
# f.seek(0)
# for line in f:
#     print(line.strip())
# f.close()

f = open("床前明月光",mode="r",encoding="utf-8")
f.seek(6)  # 3 byte == 1中文    # seek(0,2) 移动到结尾。
s = f.read(1) # 读取一个字符
print(f.tell()) # 光标在哪里？
print(s)
f.close()

# truncate(n) # 默认从文件开头截断到光标位置 如果给参数,从头截断到参数位置.




