# Leetcode 704

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1
            elif target == nums[mid]:
                return mid
            else:
                right = mid

        return -1