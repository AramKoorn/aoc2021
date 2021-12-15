from copy import deepcopy

f = open('input.txt', 'r')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
lines = [[int(j) for j in x] for x in lines]
grid = lines


# Check all directions
offset = ((-1, 0), (0, -1), (1, 0), (0, 1))


def find_shortest(grid=grid, part=2):

    # Check if inside grid
    def check(i, j):
        if i >= 0 and j >= 0 and i < n and j < m:
            return True
        else:
            return False

    # It's a square matrix which simplifies things :)
    n = len(grid)
    m = len(grid[0])

    dp = [[float('inf')] * m for x in range(n)]
    dp[0][0] = 0  # Fill in first value

    NOT_CONVERGE = True
    while NOT_CONVERGE:

        check_dp = deepcopy(dp)

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                else:
                    mn = dp[i][j]
                    for cords in offset:
                        x = i + cords[0]
                        y = j + cords[1]

                        # Inside the grid
                        if check(x, y):

                            mn = min(mn, dp[x][y] + grid[i][j])

                    dp[i][j] = mn

        if check_dp == dp:
            NOT_CONVERGE = False

    print(f'Answer part{part}: {dp[n -1][m - 1] - dp[0][0]}')

find_shortest(grid=grid, part=1)

# Make big grid
size = len(grid)
new_grid = [[0 for i in range(size*5)] for j in range(size*5)]

for y in range(5):
    for x in range(5):
        for j in range(size):
            for i in range(size):
                new_grid[y*size + j][x*size + i] = (grid[j][i] + y + x - 1) % 9 + 1

find_shortest(grid=new_grid, part=2)


if __name__ == '__main__':
    x = 2