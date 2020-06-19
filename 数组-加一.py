# -*- coding: utf-8 -*-
#project:LeetCode
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 数组-加一.py
#time: 2019/3/4 21:08
class Solution:
    def plusOne(self, digits):
        digits[len(digits) - 1] += 1
        for count in range(len(digits)-1,0 , -1):
            if digits[count] > 9:
                digits[count] %= 10
                digits[count - 1] += 1
        if digits[0] > 9:
            digits[0] %= 10
            digits.insert(0, 1)
        return digits

if __name__ == '__main__':
    s = Solution()
    digits = [9,9,9,9,9,9,9,9,9,9]
    print(s.plusOne(digits))