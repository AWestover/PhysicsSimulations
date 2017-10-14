import pprint
import random
from battle_ship_functions import *
import pygame
import pygame, sys
from pygame.locals import *


# Player view of hits/misses, player view of their own board, computer view of hits and misses, computer view of own board
boards = [[], [], [], []]

n = 10

"""

H represents a hit M represents a miss, N represents not tested

1 represents a ships pressence, 0 represents its absense, H represents a hit ship, M represents a player miss

"""

# initialize board
for i in range(0, n):
    for k in range(0, len(boards)):
        boards[k].append([])
    for j in range(0, n):
        boards[0][i].append('N')
        boards[2][i].append('N')

        boards[1][i].append('0')
        boards[3][i].append('0')





for i in range(0, 5):
    place_ship("enemy", [i, 0])
for i in range(0, 5):
    place_ship("player", [0, i])









# set up pygame
pygame.init()

# set up the window
screenDims = (500, 500)
width = int(screenDims[0]/n)
height = int(screenDims[1]/n)
mouseDown = False

windowSurface = pygame.display.set_mode(screenDims, 0, 32)
pygame.display.set_caption("Intense Battle Ship Game")



#______________________________________________________________________________-

def update_board(board_state=[]):
    for i in range(0, n):
        for j in range(0, n):
            fill_color = (250, 250, 0)
            if board_state[i][j] == "H":
                fill_color = (255, 0, 0)
            elif board_state[i][j] == "M":
                fill_color = (215, 215, 0)
            pygame.draw.rect(windowSurface, fill_color, (i*width, j*height, width, height), 1)
    pygame.display.update()


def sketch():
    if mouseDown:
        mousePos = pygame.mouse.get_pos()
        print(mousePos)
        i = int(mousePos[0]/width)
        j = int(mousePos[1]/height)
        print("h", i, j)


def exit_game():
    pygame.quit()
    sys.exit()


print("Welcome to the intenseest game of battle ship you will ever play ")
playing = True
turn = "player"


# run the game loop
while playing:
    windowSurface.fill((255, 255, 255))
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
        print_boards(turn)
        player_move()
        turn = "computer"

    else:
        print_boards(turn)
        computer_move()
        turn = "player"

    update_board(boards[0])
