# -*- coding: utf-8 -*-
# Time    : 2020/3/13 21:37
# Author  : Liu MinXuan
# Email   : liuminxuan1024@gmail.com
# File    : ADT.py


# 抽象数据类型

class Bag(object):
    def __init__(self, maxsize=10):  # 初始化类

        self.maxsize = maxsize
        self._items = list()

    # 添加数据的函数
    def add(self, item):
        if len(self) > self.maxsize:
            raise Exception("Bag is full")
        self._items.append(item)

    # 移除数据的函数
    def remove(self, item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item


def test_bag():
    bag = Bag()

    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag) == 3

    bag.remove(3)
    assert len(bag) == 2

    for i in bag:
        print(i)


test_bag()

# 选用数据结构
# 能否操作
# 效率问题
