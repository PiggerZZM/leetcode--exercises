# -*- coding: utf-8 -*-
#project:LeetCode
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 字符串-最长公共前缀.py
#time: 2019/3/6 16:45
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        result = len(strs[0])
        for i in range(0,len(strs)-1):
            count = 0
            while count < min(len(strs[i]),len(strs[i+1])):
                if strs[i][count]==strs[i+1][count]:
                    count += 1
                else:
                    break
            if result>count:
                result = count
        return strs[0][0:result]

if __name__ == '__main__':
    s = Solution()
    strs = ["flower"]
    print(s.longestCommonPrefix(strs))


