# Created by LiuMinXuan 2020/3/10 20:23 
# --coding:utf-8-
# import random
#
#
# def func():
#     c1 = chr(random.randint(1, 10))
#     c2 = chr(random.randint(1, 10))
#     c3 = chr(random.randint(1, 10))
#     return c1, c2, c3
#
#
# r1, r2, r3 = func();
#
#
# print(r1)
# print(r2)
# print(r3)

# 递归
# def test():
#     print("123")
#     print("223")
#     test()
#
#
# test()

# 递归计算阶乘


def func(n):
    if n < 1:
        print("不支持计算N小于1")
        return
    elif n == 1:
        return 1
    else:
        return func(n - 1) * n


for i in range(1, 10):
    ret = func(i)
    sum += ret
print("10的阶乘求和:", sum)



