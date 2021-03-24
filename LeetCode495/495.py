# -*- coding: utf-8 -*-
#project:LeetCode191
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 495.py
#time: 2019/2/23 21:22
class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        sum = 0
        if len(timeSeries)==0:
            return 0
        elif len(timeSeries)==1:
            return duration
        else:
            sum = duration
            for i in range(1,len(timeSeries)):
                if duration+timeSeries[i-1]>timeSeries[i]:
                    sum+=timeSeries[i]-timeSeries[i-1]
                else:
                    sum+=duration
            return sum



if __name__ == '__main__':
    s = Solution()
    time = [1,2,4]
    duration = 2
    print(s.findPoisonedDuration(time,duration))



