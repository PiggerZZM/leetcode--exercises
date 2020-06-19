# -*- coding: utf-8 -*-
#project:LeetCode
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 数组-数组交集.py
#time: 2019/3/4 20:20
class Solution:
    def intersect(self, nums1, nums2):
        result = []
        for i in nums1:
            if i in nums2:
                result.append(i)
                nums2.remove(i)
        return result

if __name__ == '__main__':
    s = Solution()
    nums1 = [4,9,5,4,6,7,8,8,6,5,3,2]
    nums2 = [9,4,9,8,4]
    print(s.intersect(nums1,nums2))

