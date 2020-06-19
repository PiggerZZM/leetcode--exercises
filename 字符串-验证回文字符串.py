# -*- coding: utf-8 -*-
#project:LeetCode
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 字符串-验证回文字符串.py
#time: 2019/3/6 11:56
class Solution:
    def isPalindrome(self, s):
        s = list(s)
        left = 0
        right = len(s)-1
        while left<right:
            while left<len(s) and (not s[left].isalnum()):
                left+=1
            while right>=0 and not (s[right].isalnum()):
                right-=1
            if left>right:
                break
            if s[left].lower()!=s[right].lower():
                return False
            else:
                left+=1
                right-=1
        return True

if __name__ == '__main__':
    s =Solution()
    string = "0pp0"
    print(s.isPalindrome(string))

