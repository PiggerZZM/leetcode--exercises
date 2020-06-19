#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：LeetCode -> 杨辉三角
@IDE    ：CLion
@Author ：Mr. An
@Date   ：2019/9/26 23:30
@Desc   ：
=================================================='''
class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        elif rowIndex == 2:
            return [1,2,1]
        else:
            third = [1,2,1]
            for i in range(3,rowIndex+1):
                left = 0
                right = 1
                result = [1]
                while right < len(third):
                    result.append(third[left]+third[right])
                    left += 1
                    right +=1
                result.append(1)
                third = result
            return third











if __name__ == '__main__':
    s = Solution()
    for index in range(1,20):
        print(s.getRow(index))

