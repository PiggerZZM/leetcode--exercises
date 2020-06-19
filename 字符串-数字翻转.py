# -*- coding: utf-8 -*-
#project:LeetCode
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 字符串-数字翻转.py
#time: 2019/3/5 21:43
class Solution:
    def reverse(self, x):
        flag = 0
        if x<0:
            x = 0-x
            flag = 1
        while x%10==0 and x !=0:
            x= x//10
        result = 0
        while x:
            result = result*10+x%10
            x = x//10
        if flag:
            if result>pow(2,31):
                return 0
            else:
                return -result
        else:
            if result >pow(2,31)-1:
                return 0
            else:
                return  result

if __name__ == '__main__':
    s =Solution()
    print(s.reverse(1534236469))