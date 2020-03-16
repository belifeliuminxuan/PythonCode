# -*- coding: utf-8 -*-
# Time    : 2020/3/14 9:18
# Author  : Liu MinXuan
# Email   : liuminxuan1024@gmail.com
# File    : 寻找数组的中心索引.py
from typing import List

# 测试
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in len(nums):
            sum += nums[i]
        for i in len(nums):
            if i == 0:
                LeftSum = 0
            else:
                LeftSum += nums[i-1]
            Rightsum = sum - LeftSum - nums[i]
        if Rightsum == LeftSum:
            return i
        return -1


