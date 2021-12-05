f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n').split('->') for x in lines]
x1y1 = [list(map(int, x[0].split(','))) for x in lines]
x2y2 = [list(map(int, x[1].split(','))) for x in lines]

# Points
points = []
for i in range(len(x1y1)):
    tmp = x1y1[i] + x2y2[i]
    points.append(tmp)

# Get dimensino
mx = 0
for x in points:
    mx = max(mx, max(x))


def walk_grid(cords, horizontal=True):
    x1, y1, x2, y2 = cords[0], cords[1], cords[2], cords[3]

    # Walk vertically
    if x1 == x2:
        # Draw the line
        for p in range(min(y1, y2), max(y1, y2) + 1):
            grid[p][x1] += 1

    # Walk horizontally
    if y1 == y2:
        # Draw the line
        for p in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][p] += 1

    # walk horizontally
    if horizontal and x1 != x2 and y1 != y2:
        moving_x1 = x1
        moving_y1 = y1

        while True:
            grid[moving_y1][moving_x1] += 1
            if moving_x1 < x2:
                moving_x1 += 1
            else:
                moving_x1 -= 1

            if moving_y1 < y2:
                moving_y1 += 1
            else:
                moving_y1 -= 1

            if moving_y1 == y2 and moving_x1 == x2:

                # Update once more
                grid[moving_y1][moving_x1] += 1
                break


def print_answer():
    overlap = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] >= 2:
                overlap += 1

    return overlap


if __name__ == '__main__':

    # Part 1
    grid = [[0] * (mx + 1) for x in range(mx + 1)]
    for cords in points:
        walk_grid(cords, horizontal=False)
    print(f'Answer part 1: {print_answer()}')

    # Part 2
    grid = [[0] * (mx + 1) for x in range(mx + 1)]
    for cords in points:
        walk_grid(cords, horizontal=True)
    print(f'Answer part 2: {print_answer()}')
