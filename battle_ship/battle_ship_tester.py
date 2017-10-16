# libraries
from battle_ship_functions import *

num_games = 10**2
moves_to_win = []

for game in range(0, num_games):

    # initialize the boards
    boards = [[], [], [], []]
    n = 10

    # initialize board
    for k in range(0, len(boards)):
        for i in range(0, n):
            boards[k].append([])
            for j in range(0, n):
                boards[k][i].append('N')

    # place ships arbitrarily
    for ship in range(0, 5):
        place_ship(boards, "player", [0, ship])
        place_ship(boards, "computer", [ship, 0])

    ct = 0
    while game_over(boards, n) == "no":
        computer_move(boards)
        ct += 1

    moves_to_win.append(total_moves_made(boards, n, 1))



avg_moves_to_win = 0
for i in range(0, len(moves_to_win)):
    avg_moves_to_win += moves_to_win[i]
avg_moves_to_win /= len(moves_to_win)

print("Moves to win statistics")
print("average " + str(avg_moves_to_win))
print("max " + str(max(moves_to_win)))
print("min " + str(min(moves_to_win)))
