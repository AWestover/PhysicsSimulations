# awestover
# this program will solve google's code jam problem
# https://codejam.withgoogle.com/codejam/contest/544101/dashboard


# read input
t = int(input())
for i in range(t):
    n, k = input().split(' ')
    n, k = int(n), int(k)
    board = []
    for j in range(n):
        board.append([int(el) for el in input()])
    print(board)


# turns a list of rows into a list of columns
def rows_to_columns(rows):
    columns = []
    for i in range(0, len(rows[0])):
        columns.append([])

    for i in range(0, len(rows)):
        for j in range(0, len(rows[i])):
            columns[j].append(rows[i][j])

    return columns



# a function which applies gravity to the current state of the board
# i.e.(that is) if board pieces are above an empty slot they will be moved down
def apply_gravity(board):
    columns = rows_to_columns(board)
    for column in columns:
        # loop through elements in this starting at the bottom and shove all '.'s to the
