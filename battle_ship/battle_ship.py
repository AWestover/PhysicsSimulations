# libraries
from battle_ship_functions import *
from pygame.locals import *
import pygame


# Player view of hits/misses,
# player view of their own board,
# computer view of hits and misses,
# computer view of own board
boards = [[], [], [], []]
n = 10

"""
Notes
H represents a hit M represents a miss, N represents Null, S represents ship pressence
"""

# initialize board
for k in range(0, len(boards)):
    for i in range(0, n):
        boards[k].append([])
        for j in range(0, n):
            boards[k][i].append('N')

# place ships arbitrarily
for i in range(0, 5):
    place_ship(boards, "enemy", [i, 0])
for i in range(0, 5):
    place_ship(boards, "player", [0, i])


# set up pygame
pygame.init()

# set up the window
screenDims = (500, 500)

width = int(screenDims[0]/n)
height = int(screenDims[1]/n)

mouseDown = False

windowSurface = pygame.display.set_mode(screenDims, 0, 32)
pygame.display.set_caption("Intense Battle Ship Game")



print("Welcome to the intenseest game of battle ship you will ever play ")
playing = True
turn = "player"


update_board(n, windowSurface, width, height, 1, boards[0])

# run the game loop
while playing:
    # WARNING: this will be run through more than once per round

    for event in pygame.event.get():
        if event.type == QUIT:
            exit_game()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                exit_game()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False

    if turn == "player":
        validMove = False
        if mouseDown:
            print_boards(boards, n, turn)
            validMove = player_move(boards, width, height)
        if validMove != False:
            turn = "computer"
            update_board(n, windowSurface, width, height, 1, boards[0])
            print("Computer take a guess")

    else:
        print_boards(boards, n, turn)
        computer_move(boards)
        turn = "player"
        update_board(n, windowSurface, width, height, 1, boards[0])
        print("Player make a guess")












#______________________________________________________________________________
