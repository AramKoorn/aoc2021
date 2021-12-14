from collections import Counter
from functools import lru_cache
import time
mp = {}
start_time = time.time()

with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if '->' not in line and line != '':
            pattern = line
        if ' -> ' in line:
            line = line.strip(' ').split(' -> ')
            mp[line[0]] = line[1]

@lru_cache(maxsize=None)
def rec(first_char, second_char, steps=2):
    if steps == 0:
        return Counter()
    else:
        new_char = mp[first_char + second_char[0]]
        return rec(new_char, second_char, steps - 1) + Counter(new_char) + rec(first_char, new_char, steps - 1)

def solve(steps=2):
    counts = Counter(pattern)
    for i in range(0, len(pattern) - 1):
        counts += rec(first_char=pattern[i], second_char=pattern[i + 1], steps=steps)

    return max(counts.values()) - min(counts.values())


#print(f"Answer part1: {solve(steps=10)}")
print(f"Answer part1: {solve(steps=10)}")
print(f"Answer part2: {solve(steps=40)}")
print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    pass