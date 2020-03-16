# -*- coding: utf-8 -*-
# Time    : 2020/3/14 12:13
# Author  : Liu MinXuan
# Email   : liuminxuan1024@gmail.com
# File    : write1.py


fd = open("test.txt", "a+")
te = str(list(range(10000000)))
fd.write(te)


