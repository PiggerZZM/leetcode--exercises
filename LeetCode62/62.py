#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/9/14 18:18
# software: PyCharm
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * m for i in range(0,n)]

        if m ==0 or n == 0:
            return 0
        else:
            for i in range(0,n):
                for j in range(0,m):
                    if i == 0 and j>=0:
                        dp[i][j] = 1
                    elif j ==0 and i>=0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]




if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(1,1))