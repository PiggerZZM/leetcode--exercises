# -*- coding: utf-8 -*-
#project:LeetCode191
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 268.py
#time: 2019/2/27 13:44
class Solution:
    def missingNumber(self, nums):
        sum = 0
        for i in range(0,len(nums)):
            sum += nums[i]
        return (len(nums)+1)*len(nums)//2 -sum


if __name__ == '__main__':
    s = Solution()
    nums = [0,5,6,8,9,4,2,3,7]
    print(s.missingNumber(nums))