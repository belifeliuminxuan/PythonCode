# -*- coding: utf-8 -*-
# Time    : 2020/3/13 22:03
# Author  : Liu MinXuan
# Email   : liuminxuan1024@gmail.com
# File    : 数组.py

# 线性结构
# 内存连续、下标访问
# 数组 内置array
# from array import array
#
# arr = array('x', 'y')

# list

# arr = [1, 2, 3, 4]
# arr.pop()
# print(arr)
# arr.append(4)
# print(arr)
# arr.insert(3, 6)
# print(arr)
# arr.remove(1)
# print(arr)


# 实现定长的Array

class Array(object):
    """
    实现定长的Array
    """

    def __init__(self, size=32):
        self.size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self.size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


def test_array():
    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1
    a.clear()
    assert a[0] == None



test_array()
