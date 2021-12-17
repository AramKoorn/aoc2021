from itertools import combinations, permutations, product
f = open('input.txt', 'r')
lines = f.readlines()
lines = [x.strip('target area: ') for x in lines]
x_line, y_line = lines[0].split(', ')[0], lines[0].split(', ')[1]

t_area = {}

for l in (x_line, y_line):
    l = l.split('=')
    t_area[l[0]] = (int(l[1].split('..')[0]), int(l[1].split('..')[1]))


def check(x, y):
    return x >= t_area['x'][0] and x <= t_area['x'][1] and y >= t_area['y'][0] and y <= t_area['y'][1]

# Brute force
cand = list(range(-31, 31))
GRID_SEARCH = product(range(t_area['x'][1] + 1), range(t_area['y'][0], abs(t_area['y'][0]) + 1))

res = -float('inf')
mem_points = set()


for points in GRID_SEARCH:
    position = (0, 0)
    x_velo, y_velo = points[0], points[1]
    mem_y = set()
    x, y = position[0], position[1]
    steps = 100

    while x <= t_area['x'][1] and y >= t_area['y'][0]:

        mem_y.add(y)
        x += x_velo
        y += y_velo
        position = (x, y)

        if check(x, y):
            res = max(res, max(mem_y))
            mem_points.add(points)
            break

        if x_velo > 0:
            x_velo -= 1
        elif x_velo < 0:
            x_velo += 1
        y_velo -= 1


print(f'Answer part1: {res}')
print(f'Answer part2: {len(mem_points)}')


if __name__ == '__main__':
    pass