# -*- coding: utf-8 -*-
#project:LeetCode191
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 470.py
#time: 2019/3/1 12:02
import random
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num = int(input())
        result = []
        i = 0
        while i<num:
            sum = 0
            for j in range(0,70):
                sum+= self.rand7()
            if sum%10:
                result.append(sum%10)
                i+= 1
        return result

    def rand7(self):
        return random.randint(0,7)



if __name__ == '__main__':
    s = Solution()
    print(s.rand10())