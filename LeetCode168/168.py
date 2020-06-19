#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/22 12:50
# software: PyCharm

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        alphe = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        result = ''
        i = 1
        while n:
            if n%26 == 0:
                n = n -1
                result = alphe[25] + result
            else:
                result = alphe[n%26-1] + result
                n = n - n%26
            n = n//26
        return result
if __name__ == '__main__':
    s = Solution()
    length = 0
    for i in range(1,1000000):
        if len(s.convertToTitle(i))>length:
            print(i,s.convertToTitle(i))
            length = len(s.convertToTitle(i))
        #print(i,s.convertToTitle(i))

    print(s.convertToTitle(4))