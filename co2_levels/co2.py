values = list(map(int, input().split()))
# print(values)

i, maxes = 2, []
l, mr = 0, [1]

while i < len(values):
    print(i, l, mr, values[i], values[l], [values[v] for v in mr])
    if values[l] >= values[mr[0]]:
        # print("l >= r")  
        l = mr[-1]
        mr = [i]
    elif values[mr[-1]] == values[i]:
        # print("continue")
        mr.append(i)
    elif values[mr[-1]] > values[i]:
        # print("ended, start new")
        l = mr[-1]
        maxes.append(mr)
        mr = [i]
        # print(maxes)
    else:
        # print("else")
        l = mr[-1]
        mr = [i]

    i += 1

for m in maxes:
    print(m[0] + 1 if len(m) == 1 else f"{m[0] + 1} {m[-1] + 1}", values[m[0]])
if not len(maxes):
    print("0 0")

# print(maxes)
