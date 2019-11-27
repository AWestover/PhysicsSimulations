"""
good tutorial-
https://pythonspot.com/generate-heatmap-in-matplotlib/
"""

import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import pdb
from pprint import pprint
import random

from functions import place_ships_randomly_cc


# Create data
n=10
boards = [[],[],[],[]]
for k in range(0, 4):
    for i in range(0, n):
        boards[k].append([])
        for j in range(0, n):
            boards[k][-1].append('N')

"""
H hit
N nulls
M miss
"""
ships = [[],[]]
ships_left = [5, 4, 3, 3, 2]
for i in range(0, 2):
    for j in range(0, 5):
        ships[i].append([])

# pdb.set_trace()
boards, ships = place_ships_randomly_cc(boards, ships, n, ships_left)



guess_map = {
    "S": "H",
    "N": "M"
}

for i in range(0, n):
    for j in range(0, n):
        if random.random() < 0.3:
            boards[2][i][j] = guess_map[boards[1][i][j]]


def dist(i, j, n):
    return abs(i-n[0]) + abs(j-n[1])

directions = []
for i in range(-1, 1):
    for j in range(-1, 1):
        if i != 0 or j != 0:
            directions.append([i, j])

def neighbors(i, j, n, depth):
    ns = []
    for de in range(1, depth):
        for d in directions:
            ii = i+de*d[0]
            jj = j+de*d[1]
            if 0<= ii < n and 0<= jj < n:
                ns.append([ii, jj])
    return ns

def heatstupid(board, n, prop=True):
    heat = []
    depth = 2
    alpha = 1000

    for row in board:
        heat.append([])
        for el in row:
            if el == 'N':
                heat[-1].append(0)
            elif el == 'H':
                heat[-1].append(n*n)
            elif el == 'M':
                heat[-1].append(-n*n)

    if prop:
        for i in range(0, n):
            for j in range(0, n):
                for nei in neighbors(i, j, n, depth):
                    d = dist(i, j, nei)
                    heat[nei[0]][nei[1]] += alpha/((10*d)**2+0.1)

    return heat

def possible_ships(board, i, j, n, length):
    # horizontal and vertical ships
    # by convention the ship starts at head_off from(above or to the left) i, j
    # and goes to the right or down

    ct = 0

    for head_off in range(0, length):
        # pdb.set_trace()
        # vertical
        vWorks=0
        if i-head_off >= 0 and i-head_off+length <= n:
            vWorks = 1
            for ii in range(i-head_off, i-head_off+length):
                if board[ii][j] == "M":
                    vWorks = 0
                    break
        # horizontal
        hWorks = 0 
        if j - head_off >= 0 and j-head_off+length <= n:
            hWorks = 1
            for jj in range(j-head_off, j-head_off+length):
                if board[i][jj] == "M":
                    hWorks = 0
                    break

        ct += hWorks + vWorks

    return ct

# difference from possible is that ships near a space that is known to have a ship are weighted higher,
# average nulls are weighted as Pr(ship there) = (total ship squares initial - number of hits) / (total squares - number of hits - number of misses)
# and hits are weighted as 1, and misses as 0s

def probable_ships(board, i, j, n, length):
    # horizontal and vertical ships
    # by convention the ship starts at head_off from(above or to the left) i, j
    # and goes to the right or down

    if board[i][j] == "M":
    	return 0
    if board[i][j] == "H":
    	return 1

    avg_pr = avg_prob(board)

    ct = 0

    for head_off in range(0, length):
        # pdb.set_trace()
        # vertical
        vWorks = 0
        if i-head_off >= 0 and i-head_off+length <= n:
            vWorks = 0
            for ii in range(i-head_off, i-head_off+length):
                if board[ii][j] == "M":
                    vWorks = 0
                    break
                elif board[ii][j] == "H":
                	vWorks += 1/length
                elif board[ii][j] == "N":
                	vWorks += avg_pr/length;
        # horizontal
        hWorks = 0 
        if j - head_off >= 0 and j-head_off+length <= n:
            hWorks = 0
            for jj in range(j-head_off, j-head_off+length):
                if board[i][jj] == "M":
                    hWorks = 0
                    break
                elif board[i][jj] == "H":
                	hWorks += 1/length
                elif board[i][jj] == "N":
                	hWorks += avg_pr/length;

        ct += (hWorks + vWorks) / (2*length)

    # print(ct, avg_pr, countInfos(board), boardSize(board))

    return ct


# counts how many misses and hits there are
def countInfos(board):
	ct = 0
	for r in board:
		for el in r:
			if el != "N":
				ct += 1
	return ct

# how many hs?
def countHs(board):
	ct = 0
	for r in board:
		for el in r:
			if el == "H":
				ct += 1
	return ct	

# average probability that a square has a ship in it, must sum to 1
def avg_prob(board):
	ships = [5,4,3,3,2]
	ct = -countHs(board)
	for s in ships:
		ct += s

	return ct / (boardSize(board) - countInfos(board))


# returns number of squares in the grid
def boardSize(board):
	# assume it is rectangular
	return len(board)*len(board[0])


b=[['N','N','N'],['M','N','M'], ['N','H','N']]

# print(possible_ships(b,1,1,3,2))
# print(probable_ships(b,1,1,3,2))

def heats_realish(board, n):
    ships_left=[5,4,3,3,2]
    heats = []
    for i in range(0, n):
        heats.append([])
        for j in range(0, n):
            c_heat = 0
            for sl in ships_left:
                # c_heat += possible_ships(board, i, j, n, sl)
                c_heat += probable_ships(board, i, j, n, sl)
            # heats[-1].append(np.log(c_heat))
            heats[-1].append(c_heat)
    return heats

def plot_ships(board):
    heat = []

    for row in board:
        heat.append([])
        for el in row:
            if el == 'N':
                heat[-1].append(0)
            elif el == 'S':
                heat[-1].append(1)
    return heat


def disp_heat(heat, ax):
    ax.imshow(heat)
    for (j,i),label in np.ndenumerate(heat):
        ax.text(i,j,round(label, 2),ha='center',va='center')

print("plotting the heatmap")

# plt.title('Battle ship heatmap')
# plt.imshow(heatstupid(boards[2], n, prop=True))

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)
fig.set_size_inches(16, 12)
plt.suptitle("Battleship")

ax1.set_title('Battle ships')
disp_heat(plot_ships(boards[1]), ax1)

ax2.set_title("Battle ship guesses")
disp_heat(heatstupid(boards[2], n, prop=False), ax2)

ax3.set_title("better heatmap")
disp_heat(heats_realish(boards[2], n), ax3)

plt.savefig("heats.png")
plt.pause(2)

