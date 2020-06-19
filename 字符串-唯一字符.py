# -*- coding: utf-8 -*-
#project:LeetCode
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 字符串-唯一字符.py
#time: 2019/3/6 11:25
class Solution:
    def firstUniqChar(self, s):
        result = {}
        s = list(s)
        for i in s:
            result[i] = result.get(i,0)+1
        for key,value in result.items():
            if value == 1:
                return s.index(key)
        return -1



if __name__ == '__main__':
    s = Solution()
    string = "loveleetcode"
    print(s.firstUniqChar(string))

