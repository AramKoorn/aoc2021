from collections import Counter


with open('input.txt', "r") as f:
    lines = f.read().splitlines()


mp = {0: 'abcefg', 1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bcdf', 5: 'abdfg', 6: 'abdefg', 7: 'acf', 8: 'abcdefg', 9: 'abcdfg'}
true_count = Counter(''.join(list(mp.values())))

# b is only value that appears 6 times
# e is only value that appears 4 tunes
# f is only value that appears 9 times

Counter(true_count.values())

inp = [x[:x.find('|')].split() for x in lines]
out = [x[x.find('|') + 2:].split() for x in lines]

# Part 1
cnt = 0
for x in out:
    cnt += sum([1 for j in x if len(j) == 2 or len(j) == 3 or len(j) == 4 or len(j) == 7])
print(f'Answer part 1: {cnt}')


def decode_digit(string, mapping):
    encoded = ''
    mapping = {v: k for k, v in mapping.items()}
    for char in string:
        encoded += char.replace(char, mapping[char])
    return encoded


def solve(line, out):

    mp_inp = {}

    for code in line:
        if len(code) == 2:
            mp_inp[code] = 1
        if len(code) == 3:
            mp_inp[code] = 7
        if len(code) == 4:
            mp_inp[code] = 4
        if len(code) == 7:
            mp_inp[code] = 8
    mp_inp_flipped = {v: k for k, v in mp_inp.items()}

    encoded = ''.join(line)
    cand_count = Counter(encoded)

    recoding_letters = {}
    for letter, freq in cand_count.items():
        if freq == 6:
            recoding_letters['b'] = letter
        if freq == 4:
            recoding_letters['e'] = letter
        if freq == 9:
            recoding_letters['f'] = letter

    recoding_letters['a'] = list(set(mp_inp_flipped[7]) - set(mp_inp_flipped[1]))[0]
    recoding_letters['c'] = list(set(mp_inp_flipped[1]) - set(recoding_letters['f']))[0]
    recoding_letters['d'] = list(set(mp_inp_flipped[4]) - set([recoding_letters['b'], recoding_letters['c'], recoding_letters['f']]))[0]
    recoding_letters['g'] = list(set(list(true_count)) - set(list(recoding_letters.values())))[0]

    decoded_output = [decode_digit(x, recoding_letters) for x in out]

    code = ''
    for x in decoded_output:
        for k, v in mp.items():
            if set(x) == set(v):
                code += str(k)

    return int(code)

res = []
for i in range(len(inp)):
    res.append(solve(inp[i], out[i]))

print(f'Answer part 2: {sum(res)}')


if __name__ == '__main__':
    x = 2