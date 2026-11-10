_, right = map(int, input().split())
cut_points = [0] + list(map(int, input().split()))
cut_points.append(right)

def cut(l, r):
    if r - l == 1:
        return 0

    cost = cut_points[r] - cut_points[l]
    mid = (cut_points[r] - cut_points[l]) / 2 + cut_points[l]

    # the left bound can't be the mid again
    temp_l, temp_r = l + 1, r
    while temp_r - temp_l > 1:
        temp_mid = (temp_l + temp_r) // 2

        if cut_points[temp_mid] < mid:
            temp_l = temp_mid + 1
        else:
            temp_r = temp_mid

    if (
        temp_l == temp_r # left over right prioritization
        or temp_r == r # temp_r is the boundary, which can't be a cut point
        or mid - cut_points[temp_l] <= cut_points[temp_r] - mid # default case
    ): new = temp_l
    else:
        new = temp_r

    print(l, r, cut_points[r], cut_points[l], cost, mid, temp_l, temp_r, new)

    return cost + cut(l, new) + cut(new, r)

print(cut(0, len(cut_points) - 1))