from copy import deepcopy


f = open("input_full.txt", "r")
lines = f.readlines()
lines = [l.split("\n") for l in lines]

grid = []
for x in lines:
    grid.append([x for x in x[0]])

n = len(grid)
m = len(grid[0])

def update_horizontal():
    set_right = set()
    make_empty = set()
    # Moving east
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            d_j = j + 1
            if d_j == m:
                d_j = 0
            if grid[i][j] == ">" and grid[i][d_j] == ".":
                set_right.add((i, d_j))
                make_empty.add((i, j))

    for i, j in set_right:
        grid[i][j] = ">"

    for i, j in make_empty:
        grid[i][j] = "."

def update_vertical():
    set_right = set()
    make_empty = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            d_i = i + 1
            if d_i == n:
                d_i = 0
            if grid[i][j] == "v" and grid[d_i][j] == ".":
                set_right.add((d_i, j))
                make_empty.add((i, j))

    for i, j in set_right:
        grid[i][j] = "v"

    for i, j in make_empty:
        grid[i][j] = "."


prev = None
i = 0
while prev != grid:
    i += 1
    prev = deepcopy(grid)
    update_horizontal()
    update_vertical()
print(i)
