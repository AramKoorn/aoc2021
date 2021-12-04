def create_input():

    f = open("input.txt", "r")
    lines = f.readlines()


    draws = [int(x) for x in lines[0].strip('\n').split(',')]

    sheet = []
    players = []
    for i in range(2, len(lines)):
        if lines[i] == '\n':
            players.append(sheet)
            sheet = []
        else:
            row = [x for x in lines[i].strip('\n').split(' ') if x != '']
            row = list(map(int, row))
            sheet.append(row)
    players.append(sheet)

    return players, draws


def check_rows(matrix, mark='x'):
    for row in matrix:
        if set(row) == {mark}:
            return True
    return False


def check_columns(matrix, mark='x'):
    values = []
    for i in range(rows):
        for j in range(cols):
            values.append(matrix[j][i])
        if set(values) == {mark}:
            return True
        else:
            values.clear()
    return False


def mark_values(matrix, value, mark='x'):

    for i in range(cols):
        for j in range(rows):
            if matrix[i][j] == value:
                matrix[i][j] = mark


def print_answer(matrix, draw):
    sm = 0
    for i in range(cols):
        for j in range(rows):
            if matrix[i][j] != 'x':
                sm += matrix[i][j]

    return sm * draw


winner = False
players, draws = create_input()
rows, cols = 5, 5

# Part 1
while not winner:
    for draw in draws:
        if winner:
            break
        for player in players:
            mark_values(matrix=player, value=draw)

            # Check win
            if check_columns(player) or check_rows(player):
                print(f'Answer part1: {print_answer(player, draw)}')
                winner = True
                break


# Part 2
players, draws = create_input()
dict_players = {i: v for i, v in enumerate(players)}
idx_players = list(dict_players)


# Use recursion
def rec(dict_players, draws):
    for i, draw in enumerate(draws):
        for k, v in dict_players.items():
            player = v
            mark_values(matrix=player, value=draw)

            # Check win
            if check_columns(player) or check_rows(player):

                # Check if last player wins
                if len(dict_players) == 1:
                    print(f'Answer part2: {print_answer(player, draw)}')
                    return

                else:
                    del dict_players[k]
                    rec(dict_players, draws[i:])
                    return


# Answer part 2
rec(dict_players, draws)


if __name__ == '__main__':
    pass