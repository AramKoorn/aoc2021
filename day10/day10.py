f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]


matching_chars = {'{': '}', '(': ')', '[': ']', '<': '>'}
matching_chars_flipped = {v: k for k, v in matching_chars.items()}

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
                print(f'bad character: {char}')
                illegal.append(char)
                return char




illegal = [find_bad_char(line) for line in lines]
illegal = [x for x in illegal if x is not None]
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
print(sum([points[x] for x in illegal]))

if __name__ == '__main__':
    pass