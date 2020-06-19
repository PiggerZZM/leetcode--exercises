#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/10/1 11:21
# software: PyCharm
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(1,len(prices)):
            if prices[i-1]<prices[i]:
                result += prices[i] - prices[i-1]
        return result




if __name__ == '__main__':
    s = Solution()
    prices = [9,5,6,8,7,4,1,2,3,6,5]
    print(s.maxProfit(prices))
