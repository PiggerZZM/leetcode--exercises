#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/9/21 20:50
# software: PyCharm
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result = []
        count = 0
        while count<length:
            if nums[count] != nums[nums[count] - 1]:
                temp = nums[count]
                nums[count] = nums[temp-1]
                nums[temp - 1 ] = temp
                count -= 1
            count += 1
        for i in range(0,length):
            if nums[i]!=i+1:
                return i+1
        return length

if __name__ == '__main__':
    s = Solution()
    nums = [4,3,2,7,8,2,3,0]
    result = s.findDuplicates(nums)
    print(result)