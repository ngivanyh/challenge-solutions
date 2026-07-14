"""
This program matches parenthesis, very straightforward

0 -> invalid
1 -> valid
"""

# string unpacking
OPEN, CLOSE = "()"

def main():
    inputs = int(input())
    brackets = [check(input().strip()) for _ in range(inputs)]

    for b in brackets: print(b)

def check(expr):
    # bit redundant here
    OPENS = expr.count(OPEN)
    if OPENS != expr.count(CLOSE):
        return 0

    i, total = 0, 0
    while i < len(expr) and total >= 0:
        total += 1 if expr[i] == OPEN else -1
        i += 1

    # but now i only have to check for negatives
    return 0 if total < 0 else OPENS

if __name__ == "__main__":
    main()