# libraries
from battle_ship_functions import *
from pygame.locals import *
import pygame

"""
Player view of hits/misses,
Player view of their own board,
Computer view of hits and misses,
Computer view of own board
"""
boards = [[], [], [], []]
n = 10
"""
H represents a hit,
M represents a miss,
N represents Null,
S represents ship pressence,
A stands for proposed ship location, (will be checked and, if it is placed in a valid location, converted to an 'S')
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
# set up the window parameters
screenDims = (500, 500)
width = int(screenDims[0]/n)
height = int(screenDims[1]/n)
cur_display_board = 0
windowSurface = pygame.display.set_mode(screenDims, 0, 32)
pygame.display.set_caption("Intense Battle Ship Game")

# basic parameters
mouseDown = False
setup = False
playing = True
turn = "player"

# initial welcome
print("Welcome to the intenseest game of battle ship you will ever play ")
update_board(n, windowSurface, width, height, 1, boards[cur_display_board])


# run the game loop
while playing:
    # check events
    for event in pygame.event.get():
        if event.type == QUIT:
            exit_game()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                exit_game()
            elif event.key == pygame.K_s:
                cur_display_board = (cur_display_board + 1) % 4
                update_board(n, windowSurface, width, height, 1, boards[cur_display_board])
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False

    if setup:

        if turn == "player":
            validMove = False
            if mouseDown:
                print_boards(boards, n, turn)
                validMove = player_move(boards, width, height)
            if validMove != False:
                turn = "computer"
                update_board(n, windowSurface, width, height, 1, boards[cur_display_board])
                print("Computer take a guess")

        elif turn == "computer":
            print_boards(boards, n, turn)
            computer_move(boards)
            turn = "player"
            update_board(n, windowSurface, width, height, 1, boards[cur_display_board])
            print("Player make a guess")

    elif not setup:
        print("Please place your pieces by clicking on the squares on which you want to place ships")















#______________________________________________________________________________
