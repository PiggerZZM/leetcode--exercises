#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
=================================================
@Project -> File   ：LeetCode -> 405转成16进制
@IDE    ：CLion
@Author ：Mr. An
@Date   ：2019/10/14 11:14
@Desc   ：
==================================================
'''
class Solution:
    def toHex(self, num):
        number = 4294967296
        if(num<0):
            num += number
        result = ''
        abc = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        while(num):
            result =  abc[num%16] + result
            num = num//16
        return result

if __name__ == '__main__':
    # print(pow(16,8))

    s = Solution()
    print(s.toHex(-1))
    # for i in range(0,1000):
    #     print(s.toHex(i))
