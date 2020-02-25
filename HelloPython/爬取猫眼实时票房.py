# Created by LiuMinXuan 2020/2/23 21:30 
# --coding:utf-8--

from urllib import request
url = 'http://piaofang.maoyan.com/second-box?beginDate=20200101'
ret_1 = request.urlopen(url)
print(ret_1.read().decode('utf-8'))

