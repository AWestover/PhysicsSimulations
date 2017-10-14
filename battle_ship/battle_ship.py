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

# resets the variables which depend on screenDims
def resize_dims(newScreenDims):
    screenDims = newScreenDims
    width = int(screenDims[0]/n)
    height = int(screenDims[1]/n)
    return (width, height, screenDims)

# set up the window parameters
width, height, screenDims = resize_dims((500, 500))
cur_display_board = 0
windowSurface = pygame.display.set_mode(screenDims, RESIZABLE)

# basic parameters
mouseDown = False
already_setup = False
playing = True
turn = "player"

# draws the board without having to input the globals
def draw_board_globals():
    update_board(n, windowSurface, width, height, 1, boards[cur_display_board], cur_display_board)

# initial welcome
print("Welcome to the intenseest game of battle ship you will ever play ")
pygame.display.set_caption("Intense Battle Ship Game")
draw_board_globals()
print("Please place your pieces by clicking on the squares on which you want to place ships")


# run the game loop
while playing:
    # check events
    for event in pygame.event.get():
        if event.type == QUIT:
            exit_game()
        # key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                exit_game()
            elif event.key == pygame.K_s:
                cur_display_board = (cur_display_board + 1) % 4
                draw_board_globals()
            elif event.key == pygame.K_d:
                # TODO: check to make sure ship stuff is valid and stuff
                already_setup = True

        # mouse interaction
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False

        # resize capability
        elif event.type==VIDEORESIZE:
            width, height, screenDims = resize_dims(event.dict['size'])
            windowSurface = pygame.display.set_mode(screenDims, RESIZABLE)
            draw_board_globals()

    if already_setup:

        if turn == "player":
            validMove = False
            if mouseDown:
                print_boards(boards, n, turn)
                validMove = player_move(boards, width, height)
            if validMove != False:
                turn = "computer"
                draw_board_globals()
                print("Computer take a guess")

        elif turn == "computer":
            print_boards(boards, n, turn)
            computer_move(boards)
            turn = "player"
            draw_board_globals()
            print("Player make a guess")

    elif not already_setup:

        if mouseDown:
            place_ship(boards, "player", get_clicked_box(width, height), tentative=True)
            draw_board_globals()








#______________________________________________________________________________
