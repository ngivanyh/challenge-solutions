"""
given an expression with:
    - TXX (10<= XX <= 99)
        magnet is at XX
    - LN (1 <= N <= 9)
        loop N times, loop ends w/ an E token
calculate how much the magnet has travelled
"""

from sys import setrecursionlimit

ASCII_0 = 48
setrecursionlimit(10000000)

def main():
    expr: str = input().strip()

    print(move(expr, 0, 0, 0)[2])

def move(expr: str, pos: int, idx: int, travelled: int):
    if idx >= len(expr): return (pos, idx, travelled)
    tok = expr[idx]

    if tok == "T":
        old_pos = pos
        pos = (ord(expr[idx + 1]) - ASCII_0) * 10 + (ord(expr[idx + 2]) - ASCII_0)
        travelled += abs(pos - old_pos) if idx else 0
        return move(expr, pos, idx + 3, travelled)
    elif tok == "L":
        iters = ord(expr[idx + 1]) - ASCII_0
        loop_start_idx = idx + 2
        for _ in range(iters):
            p, i, t = move(expr, pos, loop_start_idx, travelled)
            pos = p
            travelled = t
        idx = i + 1
        return move(expr, pos, idx, travelled)
    else: # tok is E
        return (pos, idx, travelled)

if __name__ == "__main__":
    main()