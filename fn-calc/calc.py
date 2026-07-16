"""
you are given three functions:
    f(x) = 2x - 3
    g(x, y) = 2x + y - 7
    h(x, y, z) = 3x - 2y + z

and you will be given an expression as such:
h f 5 g 3 4 3

which is equivalent to: h(f(5), g(3, 4), 3)
"""

def main():
    expr = input().strip().split()

    print(calc(expr, 0, 0)[0])


def calc(expr, idx, res):
    tok = expr[idx]

    if tok == "f":
        r, idx = calc(expr, idx + 1, res)
        return (res + (2 * r - 3), idx)

    if tok == "g":
        args = [0, 0]
        for i in range(2):
            args[i], idx = calc(expr, idx + 1, res)
        return (res + (2 * args[0] + args[1] - 7), idx)

    if tok == "h":
        args = [0, 0, 0]
        for i in range(3):
            args[i], idx = calc(expr, idx + 1, res)
        return (res + (3 * args[0] - 2 * args[1] + args[2]), idx)

    # tok is a digit
    return (int(tok), idx)


if __name__ == "__main__":
    main()