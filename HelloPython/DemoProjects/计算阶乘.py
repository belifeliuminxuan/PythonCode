# Created by LiuMinXuan 2020/3/5 20:36 
# --coding:utf-8--
ret = 1
ans = 0
for i in range(1, 21):
    ret *= i
    ans += ret

print(ans)
