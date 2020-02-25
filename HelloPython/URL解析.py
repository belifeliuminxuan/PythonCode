# Created by LiuMinXuan 2020/2/23 20:46 
# --coding:utf-8--

# from urllib import parse
#
# url = 'https://blog.csdn.net/nav/java'
# ret = parse.urlparse(url)
# print(ret.params)
# ret1 = parse.urlsplit(url)
# print(ret1)
# print(ret)
# print(ret.scheme)
# print(ret.netloc)
# print(ret.hostname)
# ParseResult(scheme='https', netloc='blog.csdn.net', path='/nav/java', params='', query='', fragment='')

from urllib import request
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36'}
rq = request.Request('https://www.baidu.com/', headers=header)
ret = request.urlopen(rq)
print(ret.read())
