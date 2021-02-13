import random


def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    return mat


# add 2 after every move
def add_new_2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2
    return mat


def move_up(grid):
    changed = False
    score = 0
    for j in range(4):
        i = 0
        while i < 4:
            if grid[i][j] != 0:
                pos = None
                for x in range(i + 1, 4):

                    if grid[i][j] == grid[x][j]:
                        pos = x
                        changed = True
                        break
                    elif grid[x][j] != 0: break

                if pos is not None:
                    grid[i][j] += grid[pos][j]
                    grid[pos][j] = 0
                    score += grid[i][j]

                x = i - 1
                while x >= 0:
                    if grid[x][j] != 0: break
                    grid[x][j] = grid[x + 1][j]
                    grid[x + 1][j] = 0
                    x -= 1
                    changed = True
            i += 1

    return grid, changed, score


def move_down(grid):
    changed = False
    score = 0
    for j in range(4):
        i = 3
        while i >= 0:
            if grid[i][j] != 0:
                pos = None
                for x in range(i - 1, -1, -1):

                    if grid[i][j] == grid[x][j]:
                        pos = x
                        changed = True
                        break
                    if grid[x][j] != 0: break

                if pos is not None:
                    grid[i][j] += grid[pos][j]
                    grid[pos][j] = 0
                    score += grid[i][j]

                x = i + 1
                while x < 4:
                    if grid[x][j] != 0: break
                    grid[x][j] = grid[x - 1][j]
                    grid[x - 1][j] = 0
                    x += 1
                    changed = True
            i -= 1

    return grid, changed, score


def move_right(grid):
    changed = False
    score = 0
    for i in range(4):
        j = 3
        while j >= 0:
            if grid[i][j] != 0:
                pos = None
                for y in range(j - 1, -1, -1):
                    if grid[i][j] == grid[i][y]:
                        pos = y
                        changed = True
                        break
                    if grid[i][y] != 0: break

                if pos is not None:
                    grid[i][j] += grid[i][pos]
                    grid[i][pos] = 0
                    score += grid[i][j]

                y = j + 1
                while y < 4:
                    if grid[i][y] != 0: break
                    grid[i][y] = grid[i][y - 1]
                    grid[i][y - 1] = 0
                    y += 1
                    changed = True
            j -= 1

    return grid, changed, score


def move_left(grid):
    changed = False
    score = 0
    for i in range(4):
        j = 0
        while j < 4:
            if grid[i][j] != 0:
                pos = None
                for y in range(j + 1, 4):

                    if grid[i][j] == grid[i][y]:
                        pos = y
                        changed = True
                        break
                    if grid[i][y] != 0: break

                if pos is not None:
                    grid[i][j] += grid[i][pos]
                    grid[i][pos] = 0
                    score += grid[i][j]

                y = j - 1
                while y >= 0:
                    if grid[i][y] != 0: break
                    grid[i][y] = grid[i][y + 1]
                    grid[i][y + 1] = 0
                    y -= 1
                    changed = True
            j += 1

    return grid, changed, score


# make any random move if possible
def random_move(grid):
    move_made = False
    move_order = [move_right, move_up, move_down, move_left]
    while not move_made and len(move_order) > 0:
        move_index = random.randint(0, len(move_order)-1)
        move = move_order[move_index]
        board, move_made, score = move(grid)
        if move_made:
            return grid, move_made, score
        move_order.pop(move_index)

    return grid, False, 0


# determine if game is over or not
def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'

    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'

    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'GAME NOT OVER'

    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return 'GAME NOT OVER'

    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return 'GAME NOT OVER'

    return 'LOST'
