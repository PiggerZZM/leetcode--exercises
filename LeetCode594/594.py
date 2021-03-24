# -*- coding: utf-8 -*-
#project:LeetCode191
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 594.py
#time: 2019/3/3 22:24
class Solution:
    # def findLHS(self, nums):
    #     result = 0
    #     nums = sorted(nums)
    #     for i in range(0,len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if max(nums[i:j+1])-min(nums[i:j+1])==1 and len(nums[i:j+1])>result:
    #                 n = nums[i:j+1]
    #                 result = len(n)
    #     return result
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # table = {}
        # for i in nums:
        #     table[i] = table.get(i, 0) + 1
        # num = [j + table.get(i + 1, -j) for i, j in table.items()]
        # if num != []:
        #     return max(num)
        # else:
        #     return 0
        # table = sorted(set(nums))
        # result = 0
        # for i in range(0,len(table)-1):
        #     if table[i+1]-table[i]==1:
        #         count1 = nums.count(table[i])
        #         count2 = nums.count(table[i+1])
        #         if result<count2+count1:
        #             result = count2+count1
        # return result
        table = {}
        for i in range(0,len(nums)):
            table[i] = table.get(i,0)+1
        nums = [j+table.get(i+1,-j) for i ,j in table.items()]
        if len(nums):
            return max(nums)
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    nums =[1,3,5,7,9,11,13,15,2,17]
    print(s.findLHS(nums))
