import random
import pygame

# print the board
def print_boards(boards, n, turn=None):
    if turn == None:
        print("player view of their hits/misses")
        for i in range(0, n):
            print(boards[0][i])

        print("player view of the enemies hits/misses relative to their ships")
        for i in range(0, n):
            print(boards[1][i])

        print("enemy view of their hits/misses")
        for i in range(0, n):
            print(boards[2][i])

        print("enemy view of the enemies hits/misses relative to their ships")
        for i in range(0, n):
            print(boards[3][i])

    elif turn == "player":
        print("player view of their hits/misses")
        for i in range(0, n):
            print(boards[0][i])

        print("player view of the enemies hits/misses relative to their ships")
        for i in range(0, n):
            print(boards[1][i])

    elif turn == "computer":
        print("enemy view of their hits/misses")
        for i in range(0, n):
            print(boards[2][i])

        print("enemy view of the enemies hits/misses relative to their ships")
        for i in range(0, n):
            print(boards[3][i])


    print("-"*200)


# place a ship at an index
def place_ship(boards, entity, index):
    if entity == "player":
        boards[1][index[0]][index[1]] = 'S'
    else:
        boards[3][index[0]][index[1]] = 'S'
    return boards


# computers move
def computer_move(boards):
    indices = [random.randint(0, 9), random.randint(0, 9)]
    guess(boards, "enemy", indices)


# players move
def player_move_terminal_input(boards):
    print("Make a guess")
    indices = [0, 0]
    indices[0] = int(input("X\t"))
    indices[1] = int(input("Y\t"))
    guess(boards, "player", indices)


# players move
def player_move(boards, width, height):
    mousePos = pygame.mouse.get_pos()
    print("Make a guess")
    index = [0, 0]
    index[0] = int(mousePos[0]/width)
    index[1] = int(mousePos[1]/height)
    guess(boards, "player", index)
    print(index)
    print("index", index[0], index[1])


# run a guess through the board states
def guess(boards, entity, index):
    res = 'M'
    if entity == "player":
        if boards[3][index[0]][index[1]] == 'S':
            res = 'H'
        boards[3][index[0]][index[1]] = res
        boards[0][index[0]][index[1]] = res

    else:
        if boards[1][index[0]][index[1]] == 'S':
            res = 'H'
        boards[1][index[0]][index[1]] = res
        boards[2][index[0]][index[1]] = res
    return boards


# ends pygame
def exit_game():
    pygame.quit()
    sys.exit()


# updates the board
def update_board(n, windowSurface, width, height, dx, board_state=[]):
    windowSurface.fill((255, 255, 255))
    for i in range(0, n):
        for j in range(0, n):
            if board_state[i][j] == "H":
                fill_color = (255, 0, 0)
            elif board_state[i][j] == "M":
                fill_color = (255, 255, 255)
            elif board_state[i][j] == "S":
                fill_color = (0, 0, 0)
            elif board_state[i][j] == "N":
                fill_color = (0, 0, 255)

            pygame.draw.rect(windowSurface, fill_color, (i*width + dx, j*height + dx, width - 2*dx, height - 2* dx), 0)

    pygame.display.update()








#______________________________________________________________________________
