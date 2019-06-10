# author azure
# 打开目标文件
# f1 = open("文件修改测试",mode="r",encoding="utf-8") as f1:
# 引入模块
import os
with open("文件修改测试",mode="r",encoding="utf-8") as f1,\
    open("文件修改测试_副本",mode="w",encoding="utf-8") as f2 :
    for line in f1:
        line = line.replace("alex","sb")
        f2.write(line)
# 删除文件
os.remove("文件修改测试")
# 重命名
os.rename("文件修改测试_副本","文件修改测试")

