# -*- coding: utf-8 -*-
#project:LeetCode191
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 136.py
#time: 2019/2/27 15:44
class Solution:
    def singleNumber(self, nums):
        num = 0
        for n in nums:
            print(num,end='')
            num = num^n
            print('^',n,'=',num)
        return num

if __name__ == '__main__':
    s = Solution()
    nums = [4,5,6,6,5,4,8]
    print(s.singleNumber(nums))
