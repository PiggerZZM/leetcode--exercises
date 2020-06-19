#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/9/26 16:15
# software: PyCharm
class Solution:
    result = []
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_len = len(s1)
        s2_len = len(s2)
        char = [0]*26
        for i in s1:
            char[ord(i)-ord('a')] = char[ord(i)-ord('a')] + 1
        result = [0] * 26
        for i in range(0,s2_len):
            if result == char:
                return True
            else:
                if i >= s1_len and i:
                    result[ord(s2[i - s1_len]) - ord('a') ] -= 1
                result[ord(s2[i]) - ord('a')] += 1
        if result == char:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    s1 = "adc"
    s2 = "dcda"
    print(s.checkInclusion(s1,s2))