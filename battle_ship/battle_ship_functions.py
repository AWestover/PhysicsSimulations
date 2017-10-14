def print_boards(turn=None):
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


def place_ship(entity, index):
    if entity == "player":
        boards[1][index[0]][index[1]] = '1'
    else:
        boards[3][index[0]][index[1]] = '1'


def computer_move():
    indices = [random.randint(0, 9), random.randint(0, 9)]
    guess("enemy", indices)


def player_move():
    print("Make a guess")
    indices = [0, 0]
    indices[0] = int(input("X\t"))
    indices[1] = int(input("Y\t"))
    guess("player", indices)


def guess(entity, index):
    res = 'M'
    if entity == "player":
        if boards[3][index[0]][index[1]] == '1':
            res = 'H'
        boards[3][index[0]][index[1]] = res
        boards[0][index[0]][index[1]] = res

    else:
        if boards[1][index[0]][index[1]] == '1':
            res = 'H'
        boards[1][index[0]][index[1]] = res
        boards[2][index[0]][index[1]] = res
