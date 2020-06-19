#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/10/1 13:11
# software: PyCharm
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        middle = 999999
        for i in range(0,len(prices)):
            middle = min(middle,prices[i])
            result = max(result,prices[i] - middle)
        return result


if __name__ == '__main__':
    s = Solution()
    prices =[7,1,5,3,6,4]
    print(s.maxProfit(prices))