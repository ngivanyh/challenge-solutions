"""
You are given a strip, with each number representing a different color
(stip = list of numbers)

1 point in the score means:
    len(set(colors[i : i+range])) == range

print the score
"""

score = 0
range_colors, _ = map(int, input().split())

colors = list(map(int, input().split()))

ITERS = len(colors) - range_colors + 1
ITERS_R = len(colors) + 1
color_freq = {}
right_color = None
left_color = None
duplicates = 0

for i in range(range_colors):
    c = colors[i]
    try:
        color_freq[c] += 1
        if color_freq[c] == 2:
            duplicates += 1
    except KeyError:
        color_freq[c] = 1

score += 1 if not duplicates else 0
left_color = colors[0]

for i in range(1, ITERS):
    color_freq[left_color] -= 1
    if color_freq[left_color] == 0:
        color_freq.pop(left_color)
    elif color_freq[left_color] == 1:
        duplicates -= 1

    left_color = colors[i]
    right_color = colors[i + range_colors - 1]

    try:
        color_freq[right_color] += 1
        if color_freq[right_color] == 2:
            duplicates += 1
    except KeyError:
        color_freq[right_color] = 1

    score += 1 if not duplicates else 0

print(score)