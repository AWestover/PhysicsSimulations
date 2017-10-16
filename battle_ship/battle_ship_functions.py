# libraries
import pygame
import random
import sys


# place a ship at an index
def place_ship(boards, entity, index, tentative=False):
    change_to = 'S'
    if tentative:
        change_to = 'A'

    if entity == "player":
        boards[1][index[0]][index[1]] = change_to
    else:
        boards[3][index[0]][index[1]] = change_to

    return boards


# computers move
def computer_move(boards, cur_player="computer"):
    goodMove = False
    while not goodMove:
        indices = [random.randint(0, 9), random.randint(0, 9)]
        goodMove = guess(boards, cur_player, indices)
    return goodMove


# gets the index of the box that the user clicked in
def get_clicked_box(width, height):
    mousePos = pygame.mouse.get_pos()
    return [int(mousePos[0]/width), int(mousePos[1]/height)]  # note int() really is just floor() for x > 0


# players move
def player_move(boards, width, height):
    index = get_clicked_box(width, height)
    result = guess(boards, "player", index)
    return result


# run a guess through the board states
def guess(boards, entity, index):
    res = 'M'
    if entity == "player":
        if boards[3][index[0]][index[1]] == 'S':
            res = 'H'
        elif boards[3][index[0]][index[1]] in ['M', 'H']:
            return False
        boards[3][index[0]][index[1]] = res
        boards[0][index[0]][index[1]] = res

    else:
        if boards[1][index[0]][index[1]] == 'S':
            res = 'H'
        elif boards[1][index[0]][index[1]] in ['M', 'H']:
            return False
        boards[1][index[0]][index[1]] = res
        boards[2][index[0]][index[1]] = res
    return boards


# ends pygame
def exit_game():
    pygame.quit()
    sys.exit()


# updates the board
def update_board(n, windowSurface, width, height, dx, board_state, cur_display_board):
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
            elif board_state[i][j] == "A":
                fill_color = (100, 100, 100, 0)

            pygame.draw.rect(windowSurface, fill_color, (i*width + dx, j*height + dx, width - 2*dx, height - 2* dx), 0)

    if cur_display_board == 0:
        pygame.display.set_caption("Player hit/miss/nulls")
    elif cur_display_board == 1:
        pygame.display.set_caption("Player ships and enemy hit/misses")
    elif cur_display_board == 2:
        pygame.display.set_caption("Computer hit/miss/nulls")
    elif cur_display_board == 3:
        pygame.display.set_caption("Computer ships and player hit/misses")

    pygame.display.update()


# terminal interaction functions

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


# players move
def player_move_terminal_input(boards):
    print("Make a guess")
    indices = [0, 0]
    indices[0] = int(input("X\t"))
    indices[1] = int(input("Y\t"))
    guess(boards, "player", indices)


# checks if the games is over
def game_over(boards, n):
    for b in range(0, 2):
        dead = True
        for i in range(0, n):
            # only need to keep looking if deadness is not disproved
            if dead:
                for j in range(0, n):
                    # first looks for ships left in player board then in computer board
                    if boards[b * 2 + 1][i][j] == 'S':
                        dead = False
                        break
        if dead:
            return 1 - b

    return "no"



#______________________________________________________________________________
