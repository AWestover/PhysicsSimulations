# alek westover
# solution to project euler 96
# solve sudoku (for all of the given boards in the input file at least)
# IMPORTANT NOTE: DIAGONALS ARE STUPID, NO ONE REALLY CARES ABOUT THEM

# useful libraries
import pprint
import pdb
from copy import deepcopy
from termcolor import colored

# import the data
boards = []
txt_file = open('p96_input_boards.txt')
for row in txt_file:
    if "Grid" in row:
        boards.append([])
    else:
        boards[-1] += [list(map(lambda x: int(x), row.replace('\n', '')))]
txt_file.close()

# functions

# this function checks to see if a group of 9 boxes
# must have a certain number put into it to satisfy the 123456789
# constraint for any row, column, diagonal, or square
def check_nine(group):
    if group.count(0) == 1:
        for i in range(0, 9):
            if i + 1 not in group:
                # missing element, index
                return i + 1, group.index(0)
    else:
        return False


# checks if there is a contradiction in a group of 9
def contradiction_in_group(group):
    #pdb.set_trace()
    for i in range(0, 9):
        if group.count(i+1) > 1:
            return True
    return False


# checks which numbers are missing from a group of nine
def missing_nums(group):
    missed = []
    for i in range(0, 9):
        if (i + 1) not in group:
            missed.append(i + 1)
    return missed


# sees which numbers are allowed in a group of 9
def not_allowed_nums(group):
    not_allowed = []
    for i in range(0, 9):
        if (i + 1) in group:
            not_allowed.append(i + 1)
    return not_allowed


# extracts the ith column from the board (left to right is 0-8 i)
def extract_column(board, i):
    # column, indices
    return [board[j][i] for j in range(0, len(board))], [[j, i] for j in range(0, len(board))]


# extracts the ith row from the board (top to bottom is 0-8 i)
def extract_row(board, i):
    return board[i], [[i, j] for j in range(0, len(board))]

"""
# extracts a diagonal from the board (1 -> bottom left to top right -1-> bottom right to top left)
def extract_diagonal(board, i):
    elements = []
    indices = []
    if i == 1:
        for j in range(0, len(board)):
            elements.append(board[len(board) - j - 1][0 + j])
            indices.append([len(board) - j - 1, 0 + j])
    else:
        for j in range(0, len(board)):
            elements.append(board[0 + j][0 + j])
            indices.append([0 + j, 0 + j])
    return elements, indices
"""

# extracts the ith 3X3 square from the board (left to right, top to bottom wrapping 0-8 i)
def extract_square(board, i):
    rows = [3*int(i/3), 3*int(i/3)+1, 3*int(i/3)+2]
    columns = [3*(i%3), 3*(i%3)+1, 3*(i%3)+2]
    elements = []
    indices = []
    for row in rows:
        for column in columns:
            elements.append(board[row][column])
            indices.append([row, column])
    return elements, indices


# generates every relevant group of 9
def relevant_groups(board):
    groups = []
    for i in range(0, 9):
        groups.append(extract_row(board, i))
        groups.append(extract_column(board, i))
        groups.append(extract_row(board, i))
    #groups.append(extract_diagonal(board, -1))
    #groups.append(extract_diagonal(board, 1))
    return groups


# gets all the groups which contain a certain entry (row, column)
def get_containing_groups(board, index):
    groups = []
    groups.append(extract_row(board, index[0]))
    groups.append(extract_column(board, index[1]))
    groups.append(extract_square(board, int(index[1]/3) + 3*int(index[0]/3) ))
    """
    if index[0] == index[1]:
        groups.append(extract_diagonal(board, -1))
    elif index[0] == len(board) - index[1] - 1:
        groups.append(extract_diagonal(board, 1))
    """
    return groups


# concatenates all of the boards elements
def concat_board(board):
    out_string = ''
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            out_string += str((board[i][j]))
    return out_string


# checks if the board is full
def completed(board):
    return '0' not in concat_board(board)


# checks if there is a contradiction in the board
def contradiction_in_board(board):
    for group in relevant_groups(board):
        if contradiction_in_group(group[0]):
            return True
    return False


# gets the indices of all spaces that are blank (0)
def get_zeros(board):
    indices = []
    for row in range(0, len(board)):
        for column in range(0, len(board[row])):
            if board[row][column] == 0:
                indices.append([row, column])
    return indices


# prints out the board aesthetically
def aesthetic_print(board, highlight_indices=[]):
    print("\n")
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] != 0:
                to_print = " " + str(board[i][j])
                if [i, j] in highlight_indices:
                    to_print = colored(to_print, "red")
                print(to_print, end=" ")
            else:
                print(" _ ", end="")
        print("\n")


# fills in the obvious ones
def fill_obvious(a_board):
    board = deepcopy(a_board)
    done = False
    while not done:
        all_groups = relevant_groups(board)
        group_vals = [all_groups[i][0] for i in range(0, len(all_groups))]
        group_indices = [all_groups[i][1] for i in range(0, len(all_groups))]
        for j in range(0, len(group_vals)):
            cur_group_info = check_nine(group_vals[j])
            if cur_group_info != False:
                c_indices = group_indices[j][cur_group_info[1]]
                c_val = cur_group_info[0]
                board[c_indices[0]][c_indices[1]] = c_val
                break
            # we are done once we get to the last group without updating the board on this round (break statement above)
            if j == len(group_vals) - 1:
                done = True
    return board


# returns all the possible values that could be placed in a square, via looking 1 move ahead
def possible_values(board, loc):
    possibilities = list(range(1, 10))
    all_containing_groups = get_containing_groups(board, loc)
    for k in range(0, len(all_containing_groups)):
        group = all_containing_groups[k][0]
        c_nas = not_allowed_nums(group)
        c_possibilities_len = len(possibilities)
        for i in range(0, c_possibilities_len):
            j = c_possibilities_len - 1 - i
            if possibilities[j] in c_nas:
                possibilities.pop(j)
    return possibilities


# experiments
def solve_board(board):
    solution = deepcopy(board)

    # first try the easy way
    solution = fill_obvious(solution)

    # k now its down to buisness with recursion
    if contradiction_in_board(solution):
        return False

    elif not completed(solution):
        possibilities = get_zeros(solution)
        for possibility in possibilities:
            guess = deepcopy(solution);
            p_one_ahead = possible_values(board, possibility)
            for i in p_one_ahead:
                guess[possibility[0]][possibility[1]] = i
                aesthetic_print(guess, highlight_indices=[possibility])
                if solve_board(guess) != False:
                    pdb.set_trace()
                    solution = guess
                    print("\n\nDONEasdfwooooooooooooooooooooooooo\n\n")
                    aesthetic_print(solution)
                    break
            """
            for i in range(0, 9):
                guess[possibility[0]][possibility[1]] = i + 1
                if solve_board(guess) != False:
                    pdb.set_trace()
                    solution = guess
                    print("\n\nDONEasdfwooooooooooooooooooooooooo\n\n")
                    aesthetic_print(solution)
                    break
            """
        return False
    else:
        print("\n\nDONE\n\n")
        aesthetic_print(solution)

    # TODO

    # SOMETHING is probably wrong with the contradiction_in_board function or something... bugus results and bogus results

    # if the puzzle is trivial we can solve it (ie only 1 value missing per column)
    # now we must employ the guess and check strategy for the rest of the board (recursively)
    # we will run through each possible index and each possible state for the index until we get a contradiction or a solved board
    # we have currently a list of all the groups that contain the index we have chosen, we need to see which moves are valid for the computer to take
    # and then take every valid move. And then propogate down the recursion
    # ie. chose a random value and then solve_board(board_with_guess) solve_board should return False if it is impossible to solve or go deeper if another guess is in order
    # we may need a better way of doing this... (more efficent)

# execute the program
# for k in range(0, len(boards)):
#         solve_board(boards[k])
# we somehow have to add these up in the end to submit to project euler...
# check how later
solve_board(boards[0])
