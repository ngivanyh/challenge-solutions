# UVa 10854

programs = int(input())

def calc(prog, i, bound):
    paths = 1

    while i < len(prog):
        if prog[i] == bound:
            break

        if prog[i] == "IF":
            i, if_paths = calc(prog, i + 1, "ELSE")
            i, else_paths = calc(prog, i + 1, "END_IF")
            paths *= if_paths + else_paths

        i += 1

    return i, paths

for _ in range(programs):
    prog = []
    while True:
        prog.append(input())

        if prog[-1] == "ENDPROGRAM":
            break

    print(calc(prog, 0, prog[-1])[1])