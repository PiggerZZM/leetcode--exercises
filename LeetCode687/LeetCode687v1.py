# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root == None:
            return 0
        root_path = 0
        if root.left != None and root.left.val == root.val:
            root_path = 1 + root_path + self.deepestPath(root.left)
        if root.right != None and root.right.val == root.val:
            root_path = 1 + root_path + self.deepestPath(root.right)
        return max(self.longestUnivaluePath(root.left), root_path, self.longestUnivaluePath(root.right))
    
    def deepestPath(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left_depth = right_depth = 0
        if root.left != None and root.left.val == root.val:
            left_depth = self.deepestPath(root.left) + 1
        if root.right != None and root.right.val == root.val:
            right_depth += self.deepestPath(root.right) + 1
        return max(left_depth, right_depth)