"""
Find the largest rectangle in a histogram:
(Bars are non-negative)

▁▂▃▄▆▅▆▇█▇▆▄▃▆
"""

BARS = int(input())

max_rect = 0
bars, stack = [], []
for i in range(BARS + 1):
    valid_i = i < BARS
    bar = int(input()) if valid_i else -1

    if valid_i:
        bars.append(bar)

    while stack and bars[stack[-1]] > bar:
        top = stack.pop()
        rect_area = bars[top] * (i if not stack else i - stack[-1] - 1)
        max_rect = max(rect_area, max_rect)

    if valid_i:
        stack.append(i)

print(max_rect)
