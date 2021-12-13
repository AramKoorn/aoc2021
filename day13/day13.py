
cords = {}
instr = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if not line.startswith('fold') and line != '':
            inp = line.split(',')
            cords[(int(inp[0]), int(inp[1]))] = True
        elif line == '':
            continue
        else:
            line = line.strip('fold along ')
            line = line.split('=')
            instr.append((line[0], int(line[1])))


for i, (axis, idx) in enumerate(instr):

    if i == 1:
        print(f'Answer part 1: {len(new_paper)}')

    new_paper = {}
    if axis == 'y':
        for points in cords.keys():
            x = points[0]
            y = points[1]
            if y > idx:
                new_point = (x, idx - (y - idx))
                new_paper[new_point] = True
            else:
                new_paper[(x, y)] = True
    if axis == 'x':
        for points in cords.keys():
            x = points[0]
            y = points[1]
            if x > idx:
                new_point = (idx - (x - idx), y)
                new_paper[new_point] = True
            else:
                new_paper[(x, y)] = True
    cords = new_paper


# Print answer part 2
x, y = max([x for x in new_paper.keys()])
res = [[' '] * (x + 1) for _ in range(y + 1)]

for x, y in new_paper.keys():
    res[y][x] = '#'

for x in res:
    print(x)

if __name__ == '__main__':
    pass