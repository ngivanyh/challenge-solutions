# Leetcode 209

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Reason to keep left in the next iteration

        nums is all positive
        right+1 increases total
        left+1 decreases total
        so,
        left-1 increases total

        and we want the *minimum* range, if left-1 only increases
        it's guaranteed to not become the minimum range
        """

        minLen = len(nums) + 1
        total = 0
        left = 0

        for right, n in enumerate(nums):
            total += n

            while total >= target:
                minLen = min(minLen, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if minLen == len(nums) + 1 else minLen
