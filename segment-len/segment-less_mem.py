"""
Memory-efficient version, merges intervals to find the big interval
"""

LINES = int(input())
BOUNDS = tuple(sorted(tuple(map(int, input().split())) for _ in range(LINES)))

cur_interval = -1
intervals = []
for l, r in BOUNDS:
    print(l, r, intervals, cur_interval)
    if cur_interval < 0: # first iteration
        intervals.append([l, r])
        cur_interval += 1
        continue

    cur_l, cur_r = intervals[cur_interval]
    if (l < cur_l and r < cur_r) or l > cur_r:
        cur_interval += 1
        intervals.append([l, r])
    elif l < cur_l <= r <= cur_r:
        intervals[cur_interval][0] = l
    elif cur_l <= l <= cur_r < r:
        intervals[cur_interval][1] = r
    elif l < cur_l and r > cur_r:
        intervals[cur_interval][0] = l
        intervals[cur_interval][1] = r

print(sum(r - l for l, r in intervals))
