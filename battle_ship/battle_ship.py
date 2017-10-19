# libraries
from battle_ship_functions import *
from pygame.locals import *
import pygame

"""
Player view of hits/misses,
Player view of their own board with computer hits and misses,
Computer view of hits and misses,
Computer view of own board with the players hits and misses

Note:
H represents a hit,
M represents a miss,
N represents Null,
S represents ship pressence,
A stands for proposed ship location, (will be checked and, if it is placed in a valid location, converted to an 'S')
D represents a ship component that is sunk
"""

n = 20
boards = [[], [], [], []]
ships = [[], []]
on_create_ship = 0
ship_types = {
    'carrier': 5,
    'detsroyer': 4,
    'boat': 3,
    'boat2': 3,
    'little_thing': 2
}

# initialize ships
for i in range(0, 2):
    for j in range(0, 5):
        ships[i].append([])

# initialize board
for k in range(0, len(boards)):
    for i in range(0, n):
        boards[k].append([])
        for j in range(0, n):
            boards[k][i].append('N')

# place ships arbitrarily
for i in range(0, 5):
    place_ship(boards, "enemy", [i, 0])

# set up pygame
pygame.init()

# set up the window parameters
width, height, screenDims = resize_dims((500, 500), n)
cur_display_board = 0
windowSurface = pygame.display.set_mode(screenDims, RESIZABLE)

# basic parameters
mouseDown = False
mouseJustReleased = False
keyJustReleased = False
already_setup = False
playing = True
turn = "player"
match_type = "pvc"
all_match_types = ["cvc", "pvc", "pvp"]
availiable_boards = 2

# draws the board without having to input the globals
def draw_board_globals():
    update_board(n, windowSurface, width, height, 1, boards[cur_display_board], cur_display_board)

# initial welcome
print("Welcome to the intenseest game of battle ship you will ever play ")
pygame.display.set_caption("Intense Battle Ship Game")
draw_board_globals()
print("Please place your pieces by clicking on the squares on which you want to place ships")

config_file = get_config("configs/config_main.cfg")
unm = input("Please input your user name\t")
if unm == config_file.get('login', 'user'):
    pwd = input("Please varify with the admin password\t")
    if pwd != config_file.get('login', 'password'):
        print("Your password did not match. You are being renamed to 'INTRUDER'")
    else:
        print("Success, you have admin privellages")
        availiable_boards = 4


# run the game loop
while playing:
    mouseJustReleased = False
    keyJustReleased = False
    # check events
    for event in pygame.event.get():
        if event.type == QUIT:
            exit_game()
        # key presses
        elif event.type == pygame.KEYDOWN:
            keyJustReleased = True
            if event.key == pygame.K_e:
                exit_game()
            elif event.key == pygame.K_s:
                cur_display_board = (cur_display_board + 1) % availiable_boards
                draw_board_globals()
            elif event.key == pygame.K_d:
                if validShipPlacement(boards, n, "player", [el for el in ship_types.values()][on_create_ship]):
                    on_create_ship += 1
                    boards[1] = destage_ships(boards[1], n, 'S')
                else:
                    boards[1] = destage_ships(boards[1], n, 'N')
                print(on_create_ship)
                draw_board_globals()

            elif event.key == pygame.K_c:
                c_mt = all_match_types.index(match_type)
                c_mt = (c_mt + 1) % len(all_match_types)
                match_type = all_match_types[c_mt]
                print("Match type", match_type)

        # mouse interaction
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
            mouseJustReleased = True

        # resize capability
        elif event.type==VIDEORESIZE:
            width, height, screenDims = resize_dims(event.dict['size'], n)
            windowSurface = pygame.display.set_mode(screenDims, RESIZABLE)
            draw_board_globals()

    if already_setup:

        if turn == "player":
            validMove = False

            if match_type == "pvc" or match_type == "pvp":
                if mouseJustReleased and cur_display_board == 0:
                    print_boards(boards, n, turn)
                    validMove = player_move(boards, width, height)
                    mouseJustReleased = False

            elif match_type == "cvc":
                if keyJustReleased:
                    validMove = True
                    validMove = computer_move(boards, cur_player="player")
                    keyJustReleased = False

            # advance turn if move was made
            if validMove != False:
                if game_over(boards, n) != "no":
                    print("game over")
                    turn = "game over"
                else:
                    turn = "computer"
                    draw_board_globals()
                    print("Computer take a guess")

        elif turn == "computer":
            if game_over(boards, n) != "no":
                print("game over")
                turn = "game over"
            else:
                print_boards(boards, n, turn)
                computer_move(boards)
                turn = "player"
                draw_board_globals()
                print(unm + " make a guess")

        elif turn == "game  over":
            print("Well, I guess that's that")

    elif not already_setup:

        if mouseJustReleased and cur_display_board == 1:
            place_ship(boards, "player", get_clicked_box(width, height), tentative=True)
            draw_board_globals()
            mouseJustReleased = False

        if on_create_ship == len(ship_types.keys()):
            already_setup = True
            print("OK " + unm + " get ready")





#______________________________________________________________________________
