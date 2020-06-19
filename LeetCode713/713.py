#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/10/9 21:14
# software: PyCharm

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        if k<0:
            return 0
        mul = 1
        left = 0
        for i in range(0,len(nums)):
            mul *= nums[i]

            while mul>=k and left <=i:
                mul /= nums[left]
                left += 1
            result += i -left + 1
        return result
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    k = 0
    print(s.numSubarrayProductLessThanK(nums,k))
