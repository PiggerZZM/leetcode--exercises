# -*- coding: utf-8 -*-
#project:LeetCode
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 937.py
#time: 2019/1/23 16:16


class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        zimu = []
        shuzi = []
        for i in range(0,len(logs)):
            if not self.is_zimu(logs[i]):
                shuzi.append(logs[i])
            else:
                zimu.append(logs[i])
        return sorted(zimu)+sorted(shuzi)
    def is_zimu(self,string):
        #string = ''
        for i in range(0,len(string)):
            if string[i]==' ':
                if string[i+1].isalpha():
                    return True
                else:
                    return False


if __name__ == '__main__':
    s = Solution()
    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    print(s.reorderLogFiles(logs))