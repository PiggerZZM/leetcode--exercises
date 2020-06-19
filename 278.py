#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/6 10:27
# software: PyCharm
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        mid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        right = len(mid)
        left = 1
        while left < right:
            m = (left + right) // 2
            # if isBadVersion(mid):
            #     right = mid
            # if not isBadVersion(left):
            #     left = mid
            if mid[m] ==1:
                right = m-1
            if mid[m] == 0:
                left = m+1
        return left



if __name__ == '__main__':
    s = Solution()
    print(s.firstBadVersion(200))
