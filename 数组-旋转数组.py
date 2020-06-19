# -*- coding: utf-8 -*-
#project:LeetCode
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 数组-旋转数组.py
#time: 2019/3/4 12:02
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        #num = nums.copy()
        # nums = [nums[(j+k)%len(nums)] for j in range(0,len(nums))]
        # print(nums)
        if k>=len(nums):
            return
        for i in range(0,len(nums)-k-1):
            temp = nums[0]
            nums.remove(nums[0])
            nums.append(temp)
        print(nums)



if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    print(s.rotate(nums,3))