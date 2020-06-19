#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/25 22:03
# software: PyCharm
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        while left<=right:
            if s[left].isalnum() or s[left].isalpha():
                if s[right].isalnum() or s[right].isalpha():
                    if s[left].lower() == s[right].lower():
                        right -=1
                        left += 1
                    else:
                        return False
                else:
                    right -=1
            else:
                left += 1
        return True
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(""))