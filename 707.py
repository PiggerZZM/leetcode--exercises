#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:andin
# datetime:2018/11/16 13:41
# software: PyCharm

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.length = 0
        #print(self.data)

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index>self.length or index<0:
            return -1
        else:
            return self.data[index]

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.data.insert(0,val)
        self.length += 1
        #print(self.data,'addAtHead')


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.data.append(val)
        self.length += 1
        #print(self.data,'addAtTail')

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < self.length:
            self.data.insert(index,val)
        elif index == self.length:
            self.data.append(val)
        #print(self.data,'addAtIndex')


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index>=0 and index <= self.length:
            self.data.pop(index)
            self.length -= 1
        #print(self.data,'deleteAtIndex')

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

if __name__ == '__main__':
    MyList = MyLinkedList()
    print(MyList.addAtHead(1),MyList.addAtTail(3),    MyList.addAtIndex(1,2),    MyList.get(1),    MyList.deleteAtIndex(1),    MyList.get(1))


