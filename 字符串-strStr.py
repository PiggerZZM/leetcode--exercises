# -*- coding: utf-8 -*-
#project:LeetCode
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 字符串-strStr.py
#time: 2019/3/6 16:22
class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        if len(haystack) == len(needle) and needle == haystack:
            return 0
        haystack = list(haystack)
        needle = list(needle)
        for i in range(0, len(haystack) - len(needle)+1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    haystack = "mississippi"
    needle = "pi"
    print(s.strStr(haystack,needle))