# Leetcode 1929

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        ans = [0] * 2 * nums_length

        for i, n in enumerate(nums):
            ans[i] = n
            ans[i + nums_length] = n

        return ans