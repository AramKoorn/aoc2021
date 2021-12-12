f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
grid = [[int(j) for j in x] for x in lines]

n = len(grid)
m = len(grid[0])

offset = ((0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1))

def check(i, j):
    if i >= 0 and j >= 0 and i < n  and j < m:
        return True
    return False


def part1(steps=100):

    res = 0

    for step in range(steps):

        flashes = set()

        # Step 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 9:
                    res += 1
                    flashes.add((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] += 1

        # Step 2
        upd = list(flashes)
        while len(upd) > 0:

            # Get last element and pop from list
            flash = upd.pop()

            for cords in offset:
                x = flash[0] + cords[0]
                y = flash[1] + cords[1]

                # Check if value is inside grid
                if check(x, y):
                    if grid[x][y] == 9 and (x, y) not in flashes:
                        res += 1
                        flashes.add((x, y))
                        upd.append((x, y))
                        grid[x][y] = 0
                    else:
                        if grid[x][y] != 0:
                            grid[x][y] += 1

        print(step)
        if step == 99:
            2
    print(res)



part1(100)






if __name__ == '__main__':
    pass