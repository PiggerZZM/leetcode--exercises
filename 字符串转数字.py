# -*- coding: utf-8 -*-
#project:LeetCode
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 字符串转数字.py
#time: 2019/3/6 14:16
class Solution:
    def myAtoi(self, str):
        flag = 0
        i = 0
        result = 0
        str = list(str)
        while i < len(str) and str[i] == ' ':
            i += 1
        if i == len(str):
            return 0
        if str[i] == '-':
            flag = 1
            i += 1
        while i < len(str) and str[i].isdigit():
            result = result * 10 + (ord(str[i]) - ord('0'))
            i += 1
        if flag:
            result = 0 - result
        if result > pow(2, 31) - 1:
            return pow(2, 31) - 1
        elif result < -pow(2, 31):
            return -pow(2, 31)
        else:
            return result


if __name__ == '__main__':
    s = Solution()
    string =  "     -42"
    print(s.myAtoi(string))