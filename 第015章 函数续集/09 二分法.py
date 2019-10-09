# author azure
# 二分查找
#  二分查找. 每次能够排除掉一半的数据. 查找的效率非常⾼. 但是局限性比较大. 必须是有
#  序序列才可以使⽤⼆分查找


# lst = [22,33,44,55,66,77,88,99,101,102,102,567,789]
# n = 67
# for el in lst:
#     if el ==n:
#         print("找到了")
#         break
# else:
#     print("没有")


# 使用二分法
# lst = [22,33,44,55,66,77,88,99,101,102,102,567,789]
# n = 88
# left = 0
# right = len(lst)-1
#
# while left < right: #边界, 当右边比左边还小的时候退出循环
#     mid = (left + right )// 2 # 必须是整除.因为索引没有小数
#     if lst[mid] > n:
#         right = mid -1
#     if lst[mid] < n:
#         left = mid +1
#     if lst[mid] ==n:
#         print("找到了")
#         break
# else:
#     print("没有")

# 递归来完成二分法
lst = [22,33,44,55,66,77,88,99,101,102,122,356,567,789,1111]
def func(n,left,right):
    if left <= right: #边界
        mid = (left+right)//2
        if n > lst[mid]:
            left = mid +1
            return func(n,left,right)  # 递归入口  # return 将结果返回
        if n < lst[mid]:
            right = mid - 1
            # 坑 函数的返回值返回给调用者。
            return func(n, left, right) # 递归入口
        if n == lst[mid]:
            print("找到了")
            return mid   # 只能通过return返回 递归出口
    else:
        print("没有这个数")
        return -1  # 只能通过return返回 递归出口
# # 找66 左边界0, 右边界:len(lst) -1
# func(66,0,len(lst) -1)
# ret = func(66,0,len(lst) -1)
# print(ret)

# lst1 = [5, 6, 7, 8]
# lst2 = [0, 0, 0, 0, 0, 1, 1, 1, 1]
# for el in lst1:
#     lst2[el] = 1
#
# lst2[4] == 1  # o(1)
