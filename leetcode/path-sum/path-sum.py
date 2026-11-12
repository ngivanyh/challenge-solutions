# Leetcode 112

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Version one, uses an extra hasSum variable and is more complicated
    """
    # def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
    #     hasSum = False

    #     def traverse(root, val_sum):
    #         nonlocal hasSum

    #         if hasSum == True:
    #             return

    #         new_sum = val_sum + root.val

    #         if root.left is None and root.right is None:
    #             hasSum = new_sum == targetSum
    #             return

    #         if root.left is None:
    #             return traverse(root.right, new_sum)

    #         if root.right is None:
    #             return traverse(root.left, new_sum)

    #         traverse(root.right, new_sum)
    #         traverse(root.left, new_sum)
    #         return

    #     if root is not None:
    #         traverse(root, 0)

    #     return hasSum

    """
    Version two, uses subtraction, the code is simpler, but it runs slower on Leetcode
    """
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False

        if root.val == targetSum and root.left is None and root.right is None:
            return True

        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
