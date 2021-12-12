from collections import Counter

f = open('input.txt', 'r')
lines = f.readlines()
caves = [x.strip('\n').split('-') for x in lines]


starts = [x for x in caves if x[0] == 'start']
other = [x for x in caves if x[0] != 'start']

# Global variable to append all succesfulll possible paths
PATHS = []
VISITED = []

def get_all_possibilities(value):
    poss = [x[1] for x in caves if x[0] == value]
    poss += [x[0] for x in caves if x[1] == value]
    poss = [x for x in poss if x != 'start']
    return poss


def rec(current, potential, twice=True):
    # Brute force all possible paths if we reach end we created a succesfull path
    poss = get_all_possibilities(current)
    if current == 'end':
        PATHS.append(potential)
        return
    for x in poss:
        if not twice:
            if x.islower() and x not in potential:
                VISITED.append(potential + [x])
                rec(x, potential + [x])
            elif x.isupper() and potential + [x] not in VISITED:
                VISITED.append(potential + [x])
                rec(x, potential + [x])
        else:
            c = Counter(potential + [x])
            n_twos = 0
            if len(c) > 0:
                for k, v in c.items():
                    if k.islower():
                        if v > 1:
                            n_twos += 1

            if x.islower() and c[x] < 3 and n_twos < 2:
                VISITED.append(potential + [x])
                rec(x, potential + [x])
            elif x.isupper() and potential + [x] not in VISITED:
                VISITED.append(potential + [x])
                rec(x, potential + [x])




rec('start', [])
print(PATHS)
print(len(PATHS))

if __name__ == '__main__':
    pass