# Leetcode 1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(((n, i) for i, n in enumerate(nums)))
        numsLength = len(nums)
        tested = set()

        def binarySearch(toSearch: int):
            left, right = 0, numsLength - 1
            while right >= left:
                mid = left + (right - left) // 2

                if toSearch < nums[mid][0]:
                    right = mid - 1
                elif toSearch > nums[mid][0]:
                    left = mid + 1
                else:
                    return mid

            return -1


        for i, n in enumerate(nums):
            n_v, n_i = n
            if n_v in tested:
                continue

            diff = target - n_v
            tested.add(n_v)
            tested.add(diff)

            if diff == n_v: # even number, clean divide
                if nums[i + 1][0] == n_v:
                    return [n_i, nums[i + 1][1]]
            else:
                diff_i = binarySearch(diff)

                if diff_i < 0:
                    continue

                return sorted([n_i, nums[diff_i][1]])

