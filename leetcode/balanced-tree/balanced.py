# Leetcode 110

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def checkBalance(node):
            if not node:
                return 0, True

            l, r = checkBalance(node.left), checkBalance(node.right)
            balanced = abs(l[0] - r[0]) <= 1
            if not l[1] or not r[1]:
                balanced = False
            # print(node.val, 1 + l[0], 1 + r[0], l[1], r[1], balanced)
            return 1 + max(l[0], r[0]), balanced

        return checkBalance(root)[1]
