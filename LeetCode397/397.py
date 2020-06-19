#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/4 18:26
# software: PyCharm

class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        time = 0
        while n > 1:
            if n%2==0:
                n = n//2
            else:
                if bin(n)[-2:] == "11" and n !=3:
                    n+=1
                elif bin(n)[-1:] == "1":
                    n-=1
            time += 1
        return time


if __name__ == '__main__':
    s = Solution()
    for i in range(3,100):
        print(i,'   ',bin(i)[-2:])
        print(s.integerReplacement(i))