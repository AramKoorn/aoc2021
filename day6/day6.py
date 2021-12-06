from functools import lru_cache


f = open("input.txt", "r")
lines = f.readlines()
fish = list(map(int, lines[0].split(',')))


@lru_cache
def rec(days, v):
    if days == 0:
        return 1
    if v != 0:
        return rec(days - 1, v - 1)
    else:
        return rec(days - 1, 6) + rec(days - 1, 8)


print(f'Answer part1: {sum([rec(18, x) for x in fish])}')
print(f'Answer part 2: {sum([rec(256, x) for x in fish])}')


if __name__ == '__main__':
    pass