# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 20:38
# @Author  : Liu MinXuan
# @Email   : liuminxuan1024@gmail.com
# @File    : 类方法.py

class test:
    """
    类方法 必须用@classmathod修饰

    """

    @classmethod
    def func(cls):
        print(cls)
        print("func 方法")

    @classmethod
    def func1(cls):
        for i in range(10):
            print(i)
    @staticmethod
    def func2():
        pass

t1 = test()
t1.func()
t1.func1()
