from PIL import Image, ImageDraw

import pdb

def updatePicture(pos, whs):

    # positive coordinates
    xs = []
    ys = []
    for p in whs:
        xs.append(p[0])
        ys.append(p[1])

    grid = [min(xs), min(ys), max(xs), max(ys)]

    im = Image.open("arena.png", 'r')
    cow = Image.open("batch/cow.png", 'r')
    wh = Image.open("wormhole.png")

    grid_transform = [int(im.size[0] / (grid[2] - grid[0] + 1)), int(im.size[1] / (grid[3] - grid[1] + 1))]

    cow = cow.resize((grid_transform[0], grid_transform[1]), Image.ANTIALIAS)
    wh = wh.resize((grid_transform[0], grid_transform[1]), Image.ANTIALIAS)

    # basewidth = grid_transform[0]
    # wpercent = (basewidth / float(cow.size[0]))
    # hsize = int((float(cow.size[1]) * float(wpercent)))
    # cow = cow.resize((basewidth, hsize), Image.ANTIALIAS)

    for p in whs:
        cx = p[0] - grid[0]
        cy = p[1] - grid[1]

        im.paste(wh, (cx*grid_transform[0], cy*grid_transform[1]))

    for p in pos:
        cx = p[0] - grid[0]
        cy = p[1] - grid[1]

        # you need cow twice because one of them allowss pasting of a transparent object onto a non transparent thing
        im.paste(cow, (cx*grid_transform[0], cy*grid_transform[1]), cow)
        # print(grid, "grid")
        # print(cow.size, "size")
        # print(im.size)
        # print(cx*grid_transform[0], cy*grid_transform[1], "coords")
        # print((p[0]*grid_transform[0], p[1]*grid_transform[1]))
        # print(im.size)

    im.save("arenaCurrent.png")
    # im.show()
#
# updatePicture([[0, 0], [1, 1], [0, 1], [1, 0]], [[0, 0], [1, 1], [0, 1], [1, 0]])
# from drawState import drawState
# drawState()
