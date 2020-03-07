# Created by LiuMinXuan 2020/3/6 22:25 
# --coding:utf-8--
# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

def findContinuousSequence(self):
    if self < 3:
        return 0
    small = 1
    big = 2
    middle = (1 + self) / 2
    curSum = small + big
    while small < middle:
        if curSum == self:
            for i in range(small, big):
                print(i)
        while curSum > self and small < middle:
            curSum -= small
            small -= 1
            if curSum == self:
                for i in range(small, big):
                    print(i)
        big += 1
        curSum += big


findContinuousSequence(9)
