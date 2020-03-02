# Created by LiuMinXuan 2020/3/1 15:27 
# --coding:utf-8--
# 打印上面一半
N = 7
# N = input("输入层数:")
for i in range(N):
    if i == 0:
        print(' ' * (N - 1 - i) + '*')
    else:
        s = ' ' * (N - 1 - i) + '*' + (i * 2 - 1) * ' ' + '*'
        print(s)
# 打印下面一半
for i in range(N - 1):
    if i == N - 2:
        print(' ' * (N - 1) + '*')
    else:
        s = ' ' * (i + 1) + '*' + (N * 2 - 5 - 2 * i) * ' ' + '*'
        print(s)
