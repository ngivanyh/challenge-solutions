"""
the user inputs the result matrix and the steps used to get there

you must print out the matrix dimensions and the original matrix
"""

def main():
    h, w, move_count = [int(v) for v in input().split()]

    matrix = []
    for _ in range(h):
        matrix.append([int(el) for el in input().split()])

    moves = [int(m) for m in input().split()]

    # print(matrix)

    for move in reversed(moves):
        # print(move)
        matrix = flip(matrix) if move else rotate(matrix)

        # print(matrix)

    print(f"{len(matrix)} {len(matrix[0])}")
    for row in matrix:
        for i, el in enumerate(row):
            print(el, end="" if i == len(row) - 1 else " ")
        print()

def flip(matrix):
    # flips the matrix from up to down
    h = len(matrix)

    for i in range(h // 2):
        temp = matrix[i]
        matrix[i] = matrix[h - i - 1]
        matrix[h - i - 1] = temp

    return matrix

def rotate(matrix):
    # rotates the matrix counter-clockwise
    new_matrix = []

    for i, val in enumerate(matrix[0]):
        col = [val]
        for j in range(1, len(matrix)):
            col.append(matrix[j][i])
        new_matrix.append(col)

    return list(reversed(new_matrix)) # quick fix to remedy the wrong append order

if __name__ == "__main__":
    main()