from collections import defaultdict

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


def rec(current, potential):
    # Brute force all possible paths if we reach end we created a succesfull path
    print(potential)
    poss = get_all_possibilities(current)
    if current == 'end':
        PATHS.append(potential)
        return
    for x in poss:
        print(poss)
        if x.islower() and x not in potential:
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