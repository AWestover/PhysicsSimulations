# libraries
import configparser as cp
import pygame
import random
import sys
import pdb


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
def computer_move(boards, ships_left=[5, 4, 3, 3, 2], cur_player="computer"):
    goodMove = False
    if cur_player == "computer":
        other_player = "player"
    elif cur_player == "player":
        other_player = "computer"
    hitMode = check_located(boards, other_player)
    while not goodMove:
        if not hitMode:
            indices = [random.randint(0, 9), random.randint(0, 9)]
        else:
            indices = hitModeShot(boards, ships_left, cur_player=cur_player)
        goodMove = guess(boards, cur_player, indices)

    return goodMove


# checks whether or not a player's ship has been located any (Hs)
def check_located(boards, player):
    if player == "player":
        player = 1
    elif player == "computer":
        player = 3
    cboard = boards[player]
    encountered = False
    for i in range(0, len(cboard)):
        for j in range(0, len(cboard[i])):
            if cboard[i][j] == 'H':
                encountered = True
    return encountered


# makes an educated guess based on the fact that we know that the ship has been hit
def hitModeShot(boards, ships_left, cur_player="computer"):
    #for i in range(-ships_left, ships_left):

    return [0, 0]

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
        todo = [1,1,1,1]
    elif turn == "player":
        todo = [1, 1, 0, 0]
    elif turn =="computer":
        todo=[0,0,1,1]

    if todo[0]:
        print("player view of their hits/misses")
        for i in range(0, n):
            print(boards[0][i])
    if todo[1]:
        print("player view of the enemies hits/misses relative to their ships")
        for i in range(0, n):
            print(boards[1][i])
    if todo[2]:
        print("enemy view of their hits/misses")
        for i in range(0, n):
            print(boards[2][i])
    if todo[3]:
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


# counts how many shots have been taken on a board (Hits + Misses)
# usefull for scoring an algorithm...
def total_moves_made(boards, n, which_board):
    move_ct = 0
    for i in range (0, n):
        for j in range(0, n):
            if boards[which_board][i][j] in ["M", "H"]:
                move_ct += 1
    #print(boards)
    return move_ct


# for easy selection of a config file
def get_config(path):
    c_config = cp.ConfigParser()
    c_config.read([path])
    return c_config


# resets the variables which depend on screenDims
def resize_dims(newScreenDims, n):
    screenDims = newScreenDims
    width = int(screenDims[0]/n)
    height = int(screenDims[1]/n)
    return (width, height, screenDims)



# checks if a ship placement is valid
def validShipPlacement(boards, n, player, cur_ship_length):
    if player == "player":
        player = 1
    elif player == "computer":
        player = 3

    cboard = boards[player]
    mark_index = []
    proposed_ct = 0
    for i in range(0, n):
        for j in range(0, n):
            if cboard[i][j] == "A":
                proposed_ct += 1

                if mark_index == []:
                    mark_index = [i, j]

    if mark_index != []:
        act_ct1 = 0
        act_ct2 = 0
        for i in range(0, cur_ship_length):
            if cboard[mark_index[0] + i][mark_index[1]]:
                act_ct1 += 1
            elif cboard[mark_index[0]][mark_index[1] + i]:
                act_ct2 += 1
        if proposed_ct == cur_ship_length:
            if (act_ct2 == 0 and act_ct1 == cur_ship_length) or (act_ct1 == 0 and act_ct2 == cur_ship_length):
                return True
        else:
            return False
    else:
        return False



# changes all of the staged ship locations to actual locations
def destage_ships(board, n, to_symbol):
    for i in range(0, n):
        for j in range(0, n):
            if board[i][j] == 'A':
                board[i][j] = to_symbol
    return board


def hash_password(pwd):
    res = 1
    for a in pwd:
        res = res*((ord(a)+1)*5791) % 7919
    return str(res)


def place_ships_randomly_cc(boards, ships, n, ships_left):
    sps = 0
    while sps < 5:
        proposed = []
        goodProposal=True

        start_loc = [random.randint(0, n-1), random.randint(0, n-1)]

        direction = [0, 0]
        direction[random.randint(0, 1)] = random.randint(0, 1)*2-1


        for loc in range(0, ships_left[sps]):
            ccx = start_loc[0]+direction[0]*loc
            ccy = start_loc[1]+direction[1]*loc
            proposed.append([ccx, ccy])
            if 0 <= ccx and ccx< n and 0 <= ccy and ccy< n:
                if boards[3][ccx][ccy] != 'N':
                    goodProposal = False
                    break
            else:
                goodProposal = False
                break

        if not goodProposal:
            continue

        for pos in proposed:
            place_ship(boards, "player", pos)
            ships[0][sps].append(pos)
            place_ship(boards, "computer", pos)
            ships[1][sps].append(pos)
        sps+=1

    return boards, ships
