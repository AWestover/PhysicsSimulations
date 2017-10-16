# libraries
from battle_ship_functions import *

num_games = 10**2
wins = 0

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
    for j in range(0, 5):
        place_ship(boards, "player", [0, i])

    while game_over(boards, n) == "no":
        computer_move(boards)

    wins += 1 - game_over(boards, n)


print("You won " + str(wins/num_games) + "% of your games")
