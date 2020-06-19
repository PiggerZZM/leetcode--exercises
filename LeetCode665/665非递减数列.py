#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
=================================================
@Project -> File   ：LeetCode -> 665非递减数列
@IDE    ：CLion
@Author ：Mr. An
@Date   ：2019/10/1 18:36
@Desc   ：
==================================================
'''
class Solution:
    def checkPossibility(self, nums):
        left = 0
        result = 0
        while left< len(nums):
            if result >= 2:
                return False
            if nums[left] > max(nums[left+1:]):
                result += 1
            left += 1

        return True



if __name__ == '__main__':
    s = Solution()
    nums =  [4,2,1]

    print(s.checkPossibility(nums))




