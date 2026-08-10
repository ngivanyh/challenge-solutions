"""
difference array method (uses a lot of memory)

given the left and right bounds of a set amount of lines,
calculate how much length they cover
"""

LINES = int(input())
BOUNDS = tuple(tuple(map(int, input().split())) for _ in range(LINES))

LEFT_BOUND = min(BOUNDS, key=lambda k: k[0])[0]
RIGHT_BOUND = max(BOUNDS, key=lambda k: k[1])[1]
diff_arr = [0] * (RIGHT_BOUND - LEFT_BOUND + 1)

for l, r in BOUNDS:
    diff_arr[l - LEFT_BOUND] += 1
    diff_arr[r - LEFT_BOUND] -= 1

length, current = 0, 0
for i in range(RIGHT_BOUND - LEFT_BOUND + 1):
    current += diff_arr[i]
    length += 1 if current > 0 else 0

print(length)