f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
grid = [[int(x) for x in x] for x in lines]

rows = len(grid)
cols = len(grid[0])

offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def check_adj(i, j):
    curr_val = grid[i][j]
    for cords in offset:
        # Ignore if we are out of bounds
        try:
            if grid[i + cords[0]][j + cords[1]] <= curr_val:
                return 0
        except:
            continue

    # All points are lower
    return 1 + curr_val


res = 0
for i in range(rows):
    for j in range(cols):
        res += check_adj(i, j)

print(f"Answer part1: {res}")


def check(i, j):
    if i >= 0 and j >= 0 and i <= rows - 1 and j <= cols - 1:
        return True
    else:
        return False


def rec(i, j, st):

    if check(i, j) :
        if (i, j) not in st and grid[i][j] < 9:
            st.add((i, j))
            for cords in offset:
                rec(i + cords[0], j + cords[1], st)
    return st


memory = set()
res = []
for i in range(rows):
    for j in range(cols):
        if (i, j) not in memory:
            points = rec(i, j, set())
            memory.update(points)
            res.append(len(points))

most = sorted(list(res))[-3:]
ans = 1
for x in most:
    ans *= x
print(f'Answer part2: {ans}')


if __name__ == '__main__':
    pass