# Leetcode 101

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = valx
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def isMirror(l, r):
            if not l and not r:
                return True

            if not l or not r:
                return False

            return l.val == r.val and isMirror(l.right, r.left) and isMirror(l.left, r.right)

        return isMirror(root.left, root.right) if root else True