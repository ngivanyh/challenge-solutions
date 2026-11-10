# Leetcode 145

from sys import setrecursionlimit

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    setrecursionlimit(1000000)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traverse_n_v = []

        dfs_stack = [root]

        while len(dfs_stack):
            node = dfs_stack.pop()
            if not node:
                continue

            dfs_stack.append(node.left)
            dfs_stack.append(node.right)
            traverse_n_v.append(node.val)

        return traverse_n_v[::-1]
