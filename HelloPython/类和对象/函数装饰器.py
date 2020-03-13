# -*- coding: utf-8 -*-
# Time    : 2020/3/13 21:13
# Author  : Liu MinXuan
# Email   : liuminxuan1024@gmail.com
# File    : 函数装饰器.py


def func(test):
    print("func 函数")

    def ab():
        print("123")

    return ab()


@func
def test():
    print("test 函数")


print(test)
