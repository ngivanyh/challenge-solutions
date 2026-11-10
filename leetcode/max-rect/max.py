# Leetcode 84
# Similar to largest-rect in Stack-Recursion/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_h = 0
        heights.append(-1)
        stack = [-1]

        for i, height in enumerate(heights):
            if height >= heights[stack[-1]]:
                stack.append(i)
                continue

            while len(stack) and height < heights[stack[-1]]:
                bar = stack.pop()
                max_h = max(
                    max_h,
                    (i - stack[-1] - 1) * heights[bar]
                )

            stack.append(i)

        return max_h