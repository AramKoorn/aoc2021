f = open("input.txt", "r")
lines = f.readlines()

# Formatting
lines = [x.strip('\n').split(' ') for x in lines]

# Part 1 
x, y = 0, 0

for val in lines:
    value = int(val[1])
    if val[0] == 'up':
        y += value
    if val[0] == 'down':
        y -= value
    if val[0] == 'forward':
        x += value

print(f'Answer part 1: {-y * x}')

# Part 2 
x, y, aim = 0, 0, 0

for val in lines:
    value = int(val[1])
    if val[0] == 'up':
        aim -= value
    if val[0] == 'down':
        aim += value
    if val[0] == 'forward':
        x += value
        y -= value * aim


print(f'Answer part 2: {-y * x}')
