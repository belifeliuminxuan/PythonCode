# from urllib import request

# count = 1
# while count < 10:
# request.urlretrieve('http://a3.att.hudong.com/68/61/300000839764127060614318218_950.jpg', 'sougou%count.jpg')
# count += 1

# 编码
# from urllib import parse
# data = {'name': '爬虫基础', 'sex': '男', 'years': '23'}
# 函数操作字典
# qs = parse.urlencode(data)
# print(qs)
# 对字符串进行编码处理

from urllib import parse

str_ = 'Hello我的World'

ret = parse.quote(str_)

print(ret)
# 解码

print(parse.parse_qs(ret))
