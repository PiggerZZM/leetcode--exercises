# -*- coding: utf-8 -*-
#project:LeetCode
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 字符串-字母异位词.py
#time: 2019/3/6 11:49
class Solution:
    def make_dict(self,s):
        result = {}
        for i in s:
            result[i] = result.get(i,0)+1
        return result
    def isAnagram(self, s, t):
        s = self.make_dict(s)
        t = self.make_dict(t)
        if s == t:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    string1 = "anagrbm"
    string2 = "anagrma"
    print(s.isAnagram(string1,string2))

