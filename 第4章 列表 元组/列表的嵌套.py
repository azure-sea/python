# author azure
lst = ["Azure","gay","wusir",["binbin","李冰",[1,"火锅","ritian","复制"],"王彬"]]
# print(lst[3][2][1]) #火锅
lst[3][2][2] = lst[3][2][2].upper() #将ritian替换成大写
print(lst)

lst[3][2][0] = lst[3][2][0] +99
print(lst)