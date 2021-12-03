f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]


def find_most_common(ls, pos):
    ones, zeros = 0, 0

    for x in ls:
        if x[pos] == '0':
            zeros += 1
        else:
            ones += 1
    
    if zeros == ones:
        ones += 1

    return "1" if ones > zeros else "0"

gamma_rate = ''

for x in range(len(lines[0])):
    gamma_rate += find_most_common(lines, x)

# Flip gamma rate
epsilon_rate = ''.join(['1' if x == '0' else '0' for x in gamma_rate])
print(f'Answer part1: {int(gamma_rate, 2) * int(epsilon_rate, 2)}')

## Part 2

def keep_rows(ls, value, pos):
    
    res = []
    for x in ls:
        if x[pos] == value:
            res.append(x)
    return res    

def find_least(ls, pos):
    ones, zeros = 0, 0

    for x in ls:
        if x[pos] == '0':
            zeros += 1
        else:
            ones += 1
    
    if zeros == ones:
        ones += 1

    return "1" if ones < zeros else "0"

def find(candidates, what='common'):

    for i in range(len(candidates[0])):
        
        # Find most
        if what == 'common':
            most_common = find_most_common(candidates, pos=i)
        else:
            most_common = find_least(candidates, pos=i)

        # Remove all rows
        candidates = keep_rows(ls=candidates, value=most_common, pos=i).copy()

        if len(candidates) == 1:
            return candidates[0]

candidates = lines.copy()

val1 = find(candidates, what='common')
val2 = find(candidates, what='least')
print(f'Answer part2: {int(val1, 2) * int(val2, 2)}')