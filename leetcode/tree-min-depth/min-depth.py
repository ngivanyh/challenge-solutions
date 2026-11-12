# Leetcode 111

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        l, r = self.minDepth(root.left), self.minDepth(root.right)

        if root.left is None:
            return 1 + r

        if root.right is None:
            return 1 + l

        return 1 + min(r, l)