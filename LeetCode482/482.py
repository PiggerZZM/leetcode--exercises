# -*- coding: utf-8 -*-
#project:LeetCode191
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 482.py
#time: 2019/3/3 11:24
class Solution:
    def licenseKeyFormatting(self, S, K):
        count = 0
        result = ""
        i = len(S)-1
        while i>=0:
            if not S[i] == '-':
                if count == K:
                    result = '-'+ result
                    count = 0
                result = S[i]+result
                count +=1
            i = i-1
        return result.upper()

if __name__ == '__main__':
    s = Solution()
    S = "2-5g-3-J"
    K = 2
    print(s.licenseKeyFormatting(S,K))









