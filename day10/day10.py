f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]


matching_chars = {'{': '}', '(': ')', '[': ']', '<': '>'}
matching_chars_flipped = {v: k for k, v in matching_chars.items()}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

pairs = [('(', ')'), ('<', '>'), ('{', '}'), ('[', ']')]
open_chars = '({[<'
closing_chars = ')}]>'


def find_bad_char(line):

    op = []
    close = []
    illegal = []

    for char in line:
        if char in open_chars:
            op.append(char)
            close.append(matching_chars[char])  # add matching closing char to list
        # Its a closing character
        else:
            matching_open_char = matching_chars_flipped[char]
            cand = op.pop()
            if cand != matching_open_char:
                #print(f'bad character: {char}')
                illegal.append(char)
                return char


def find_bad_char_part2(line):

    op = []
    close = []

    for char in line:
        if char in open_chars:
            op.append(char)
            close.append(matching_chars[char])  # add matching closing char to list
        # Its a closing character
        else:
            matching_open_char = matching_chars_flipped[char]
            cand = op.pop()
            op
            if cand != matching_open_char:
                return None

    # We haven't found bad character but we still need to complete the rest in op
    need_to_match = op[::-1]
    seq = [matching_chars[x] for x in need_to_match]
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    seq = [points[x] for x in seq]

    score = 0
    for x in seq:
        score = (score * 5) + x

    return score

# Part 1
illegal = [find_bad_char(line) for line in lines]
illegal = [x for x in illegal if x is not None]
print(f'Answer part1: {sum([points[x] for x in illegal])}')

# Part 2
part2 = [find_bad_char_part2(line) for line in lines]
part2 = [x for x in part2 if x is not None]
print(f'Answer part 2: {sorted(part2)[len(part2) // 2]}')

if __name__ == '__main__':
    pass