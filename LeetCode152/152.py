#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/10/10 15:55
# software: PyCharm


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_number = nums[0]
        count = 1
        left = 0
        if len(nums)==0:
            return 0
        for num in nums:
            count *= num
            if count>=max_number:
                max_number = count
            else:
                if not nums[left]==0:
                    count = count/nums[left]
                left += 1
        return max_number

if __name__ == '__main__':
    s = Solution()
    nums = [2,3,-2,4]
    print(s.maxProduct(nums))