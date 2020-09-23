# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    count = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.deepestPath(root)
        return self.count
    
    def deepestPath(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left_depth = self.deepestPath(root.left)
        right_depth = self.deepestPath(root.right)
        root_path = 0
        root_left = root_right = 0
        if root.left != None and root.val == root.left.val:
            root_path += 1 + left_depth
            root_left = 1 + left_depth
        if root.right != None and root.val == root.right.val:
            root_path += 1 + right_depth
            root_right = 1 + right_depth
        
        self.count = max(self.count, root_path)
        return max(root_left, root_right)