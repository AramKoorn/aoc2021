f = open("input.txt", "r")
lines = f.readlines()
crabs = list(map(int, lines[0].split(',')))

# Brute force
cand = list(range(min(crabs), max(crabs) + 1))


def cost_function(n):
    return (n * (n + 1)) / 2


def make_equal(ls, c, part='part2'):

    cnt = 0

    if part == 'part2':
        for x in ls:
            cnt += cost_function(abs(x - c))
    else:
        for x in ls:
            cnt += abs(x - c)
    return cnt


if __name__ == '__main__':

    # part 1
    print(f'Answer part1: {min([make_equal(crabs, x, "part1") for x in cand])}')

    # part 2
    print(f'Answer part2: {min([make_equal(crabs, x, "part2") for x in cand])}')

