"""
"""

def main():
    expr = input().strip()

    print(move(expr, 0, 0, 0)[2])

def move(expr, pos, idx, travelled):
    if idx >= len(expr): return (pos, idx, travelled)
    tok = expr[idx]

    if tok == "T":
        old_pos = pos
        pos = int(expr[idx+1 : idx+3])
        travelled += abs(pos - old_pos) if idx else 0
        return move(expr, pos, idx + 3, travelled)
    elif tok == "L":
        iters = int(expr[idx + 1])
        for _ in range(iters):
            p, i, t = move(expr, pos, idx + 2, travelled)
            pos = p
            travelled = t
        idx = i + 1
        return move(expr, pos, idx, travelled)
    else: # tok is E
        return (pos, idx, travelled)

if __name__ == "__main__":
    main()