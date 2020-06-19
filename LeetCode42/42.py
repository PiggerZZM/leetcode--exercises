# -*- coding: utf-8 -*-
#project:LeetCode
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 42.py
#time: 2019/2/28 11:45
class Solution:
    def trap(self, height):
        all = 0
        for i in range(0,len(height)):
            if height[i] !=0:
                left = i
                break
        if len(height)<=2:
            return 0
        else:

                # if height[left]<=height[right] and height[right]>height[right-1]:#左边小于右边且右边的点是一个极大值点。
                #     mid = height[left]
                #     flag = 1
                # elif height[left]>=height[right]:#左边大于等于
                #     if right<len(height)-1:
                #         if height[right]>=height[right+1]:
                #             mid = height[right]
                #             flag = 1
                #         else:
                #             right += 1
                #     else:
                #         mid = height[right]
                #         flag = 1
                # else:
                #     right += 1
                #     continue
            right = left + 1
            mid = 0
            flag = 0
            while right < len(height):
                if right < len(height)-1:
                    if height[right]>=height[right-1] and height[right]>=height[right+1]:
                        if height[left]>height[right]:
                            if not height[right]<max(height[right+1:]):
                                mid = min(height[left],height[right])
                                flag = 1
                            else:
                                right += 1
                        else:
                            mid = min(height[left], height[right])
                            flag = 1
                    else:
                        right += 1
                if right == len(height)-1:
                    mid = min(height[left], height[right])
                    flag = 1
                if flag:
                    for i in range(left, right):
                        if mid - height[i] > 0:
                            all += mid - height[i]
                    left = right
                    right += 1
                    flag = 0
            return all
if __name__ == '__main__':
    s = Solution()
    nums = [2,1,2]
    print(s.trap(nums))




