#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/9/16 12:13
# software: PyCharm
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        right = head
        count = 1
        pre = ListNode(0)
        pre.next = head
        left = pre
        while right !=None:
            if count%k == 0:
                left = self.reverse(left,right.next)
                right = left.next
            else:
                right = right.next
            count += 1
        return pre.next

    def reverse(self,left,right):
        l = left.next
        r = l.next
        while r != right:
            l.next = r.next
            r.next = left.next
            left.next = r
            r = l.next
        return l


if __name__ == '__main__':
    s = Solution()
    node = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    head = ListNode(-1)

    p = head
    for i in node:
        pr = ListNode(i)
        p.next = pr
        p = pr

    p = s.reverseKGroup(head.next,5)

    while p != None:
        print(p.val)
        p = p.next

