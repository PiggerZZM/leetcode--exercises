#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:andin
# datetime:2018/11/14 11:25
# software: PyCharm
class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.deque = list()
        self.length = 0
        self.size = k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.deque.insert(0,value)
        self.length += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.deque.append(value)
        self.length += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.deque.pop(0)
        self.length -= 1
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.deque.pop()
        self.length -= 1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.deque[0]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            result = self.deque[self.length - 1]
            return result

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if self.length == 0:
            return True
        else:
            return False

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if self.length >= self.size:
            return True
        else:
            return False

if __name__ == '__main__':
    """["MyCircularDeque", "insertFront", "getFront", "isEmpty", "deleteFront", "insertLast", "getRear", "insertLast","insertFront", "deleteLast", "insertLast", "isEmpty"][[8], [5], [], [], [], [3], [], [7], [7], [], [4], []]"""
    circularDeque = MyCircularDeque(8)
    print(circularDeque.insertFront(5),circularDeque.getFront(),circularDeque.isEmpty(),circularDeque.deleteFront()
        ,circularDeque.insertLast(3),circularDeque.getRear(),circularDeque.insertLast(7),circularDeque.insertFront(7),circularDeque.deleteLast(),circularDeque.insertLast(4),circularDeque.isEmpty())
