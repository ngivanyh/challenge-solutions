"""
user provides a expression and grid dimensions (n*n)

if the character is '1', the sum is set to n*n
if the character is '0', nothing is added
if the character is '2', the grid is split into four quadrants, each having a 1 or 0

print the total sum
"""

def main():
    expr = input()
    grid_dim = int(input())
    print(evaluate(expr, 0, grid_dim)[0])

def evaluate(expr, idx, grid_dim, sum=0):
    if expr[idx] == '1':
        sum = grid_dim * grid_dim
    elif expr[idx] == '2':
        for _ in range(4):
            add, idx =  evaluate(expr, idx + 1, grid_dim // 2)
            sum += add
    return (sum, idx)

if __name__ == "__main__":
    main()