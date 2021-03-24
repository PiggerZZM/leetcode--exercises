# -*- coding: utf-8 -*-
#project:LeetCode191
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 137.py
#time: 2019/2/27 16:04
class Solution:
    def singleNumber(self, nums):
        num =0
        for n in nums:
            n = num and n
            num = num ^ n
        return num
if __name__ == '__main__':
    s = Solution()
    nums = [4,4,5,4]
    print(s.singleNumber(nums))
