"""
inputted with:
    1. n trees and a max right coord
    2. the positions of these n trees
    3. the heights of these n trees

the trees are arranged in a line

when you cut down a tree, you must check that it
doesn't exceed the left and right limits and doesn't
touch the trees next to it, so:
    tree_pos - tree_height >= left tree pos
    tree_pos + tree_height <= right tree pos

print the trees cut and the tallest tree cut
"""

trees, RIGHT = map(int, input().split())
LEFT = 0

tree_pos = list(map(int, input().split()))
tree_heights = list(map(int, input().split()))

ranges = [(pos - height, pos + height, pos, height) for pos, height in zip(tree_pos, tree_heights)]

def cut_tree():
    cut = []
    for i, range in enumerate(ranges):
        l, r, _, __ = range
        # print(range)

        p_l = ranges[i - 1][2] if i else LEFT
        p_r = ranges[i + 1][2] if i + 1 < len(ranges) else RIGHT

        l_ok =  p_l <= l and p_l >= LEFT
        r_ok =  p_r >= r and p_r <= RIGHT

        if l_ok or r_ok:
            cut.append(i)

        # print(cut)
    return cut

cut = 0
cut_heights = []
while cut_idx := cut_tree():
    # print(ranges, cut_idx)
    for correction, i in enumerate(cut_idx):
        cut_heights.append(ranges.pop(i - correction)[3])

    cut += len(cut_idx)
    # print(ranges)

print(cut, max(cut_heights) if cut_heights else 0, sep="\n")