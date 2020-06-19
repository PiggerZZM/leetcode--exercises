#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:andin
# datetime:2018/11/18 17:38
# software: PyCharm
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 :
            return 0
        elif len(nums) == 1:
            return 1
        result = 1
        max_result = 1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                result += 1
                if result > max_result:
                    max_result = result
            else:
                result = 1
        return max_result

if __name__ == '__main__':
    s = Solution()
    nums = [1,3,5,4,2,7]
    print(s.findLengthOfLCIS(nums))