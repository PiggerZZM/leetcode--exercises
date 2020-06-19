#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/9/23 11:31
# software: PyCharm


class Solution:
    result = []
    def checkInclusion(self, s1, s2, index, length):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        self.make(list(s1),index,length)
    def make(self,s1,index,length):
        if index == length -1:
            return
        for i in range(index,length-1):
            print(''.join(s1))
            temp = s1[i]
            s1[i] = s1[i+1]
            s1[i+1] = temp
            self.make(s1,i+1,length)

        return


if __name__ == '__main__':
    s = Solution()
    s1 = '1234'
    s2 = '345'
    s.checkInclusion(s1,s2,0,len(s1))