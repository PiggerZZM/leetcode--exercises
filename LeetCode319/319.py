#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/9/26 21:11
# software: PyCharm
import math
class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """


        return int(math.sqrt(n))




if __name__ == '__main__':
    s = Solution()

    print(s.bulbSwitch(10))