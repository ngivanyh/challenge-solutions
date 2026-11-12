# Leetcode 144

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        dfs_stack = [root]
        traverse_n_v = []

        while len(dfs_stack):
            node = dfs_stack.pop()
            if not node:
                continue

            dfs_stack.append(node.right)
            dfs_stack.append(node.left)
            traverse_n_v.append(node.val)

        return traverse_n_v