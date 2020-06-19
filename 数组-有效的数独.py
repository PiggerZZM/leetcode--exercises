# -*- coding: utf-8 -*-
#project:LeetCode
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 数组-有效的数独.py
#time: 2019/3/7 11:44
class Solution:
    def isValidSudoku(self, board):
        row = 0
        col = 0
        for row in range(0,9):
            nums = []
            nums1 = []
            for col in range(0,9):
                if board[row][col] in nums:
                    return False
                if board[row][col].isdigit():
                    nums.append(board[row][col])
            for col in range(0,9):
                if board[col][row] in nums1:
                    return False
                if board[col][row].isdigit():
                    nums.append(board[col][row])
        for i in range(0,3):
            for j in range(0,3):









if __name__ == '__main__':
    s = Solution()
    board = []
    print(s.isValidSudoku(board))

