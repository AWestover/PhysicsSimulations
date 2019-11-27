# checkers

import pygame, sys, random
from pygame.locals import *
import pdb

pygame.init()
screen_dims = [700, 700]
window = pygame.display.set_mode((screen_dims[0], screen_dims[1]), RESIZABLE)
font = pygame.font.SysFont(None, 30)
screen_color = (0, 10, 10)
n = 8  # board size (Note the board must be a square...)


# what pygaem should do when ending the program
def end_program():
    pygame.quit()
    sys.exit()
    return False


# creates a blank board
def clear_board():
    board = []
    for i in range(0, n):
        board.append([])
        for j in range(0, n):
            board[i].append(0)
    return board


# sets the board to the start state
def start_board(board):
    off = 0
    for j in range(0, n):  # row (y)
        for i in range(0, n):  # column (x)
            if j < int(n/3) + 1:  # top third of board
                if (i + off) % 2 == 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
            elif int(n/3) + 1 <= j < int(2*n/3):  # middle
                board[i][j] = 0
            else:  # bottom third
                if (i + off) % 2 == 0:
                    board[i][j] = -1
                else:
                    board[i][j] = 0
        off += 1
    return board


# draws the board
def display_board(board, highlight_indices=[]):  # column, row
    for i in range(0, n):  # what column are we on (x)
        for j in range(0, n):  # what row are we on (y)
            cpos = [i*screen_dims[0]/n, j*screen_dims[1]/n]
            ccolor = (0, 0, 0)
            if board[i][j] == 1:
                ccolor = (255, 0, 0)
            elif board[i][j] == -1:
                ccolor = (0, 255, 0)
            if [i, j] in highlight_indices:
                ccolor = (int(0.2*ccolor[0]) + 100, int(0.2*ccolor[1]) + 100, int(0.2*ccolor[2]), 90)
            pygame.draw.rect(window, ccolor, (cpos[0], cpos[1], screen_dims[0]/n, screen_dims[1]/n))


# generic procedure for selecting a square, no error catching for selecting the wrong side or an empty square yet...
def update_select(selected, key):
    if key == pygame.K_UP:
        selected[1] = (selected[1] - 1) % n
    elif key == pygame.K_DOWN:
        selected[1] = (selected[1] + 1) % n
    elif key == pygame.K_LEFT:
        selected[0] = (selected[0] - 1) % n
    elif key == pygame.K_RIGHT:
        selected[0] = (selected[0] + 1) % n
    elif key == pygame.K_SPACE:
        return "DONE"
    display_board(board, highlight_indices=[selected])
    return selected

# helps the user perform a move
def user_move(board, player):
    select_square()


# initialize the board
board = start_board(clear_board())
display_board(board)
turn = "player1"
last_selected = [0, 0]
selecting = False

# the game loop
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = end_program()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                running = end_program()
        elif event.type == pygame.KEYUP:
            if selecting:
                val = update_select(last_selected, event.key)
                if val != "DONE":
                    last_selected = val

    pygame.display.update()

    if turn == "player1":
        selecting = True
        """
        if val != "DONE":
            last_selected = val
        else:
            turn = "player2"
        """
