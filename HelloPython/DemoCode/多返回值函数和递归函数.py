# Created by LiuMinXuan 2020/3/3 11:14 
# --coding:utf-8--

# 多返回值函数实际上返回的是元组
# 程序既可以返回元素，也可以直接返回多个值


# def test(a, b, c):
#     return a, b, c
#
#
# print(test(1, 2, 3))
# 返回值的时候，系统自动封包为元组

# my_list = [1, 2, 3, 4, 5]
# it = iter(my_list)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# my_list = list(range(1, 11))
# it = iter(my_list)
# for i in it:
#     print(i)
# class test:
#     """
#     test
#     """
#     a = 10

# my_list = list(range(1, 11))
# for i in my_list:
#     print(i)


# my_tuple = (1, 2, 3, 4, 5, 6, 7)

# it = iter(my_tuple)
# for i in it:
#     print(i)

# import os
# os.getcwd()

# def func():
#     print()

import time

t = time.time()

print(t)
