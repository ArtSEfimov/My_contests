# Код писать сюда \(❤‿❤)/
# Код писать сюда \(❤‿❤)/
N = int(input())

field = [[] for i in range(N + 2)]
for i in range(N + 2):
    if i == 0 or i == N + 1:
        field[i] = [0] + [0 for i in range(N)] + [0]
    else:
        field[i] = [0] + [int(i) for i in list(input())] + [0]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == 1 and j == 1 or i == N and j == N:
            pass
        else:
            if field[i - 1][j] == 0 and field[i][j - 1] == 0:
                field[i][j] = 0
            else:
                if field[i][j] != 0:
                    local_sum = field[i][j - 1] or field[i - 1][j] if 0 in (field[i][j - 1], field[i - 1][j]) else min(
                        field[i][j - 1], field[i - 1][j])
                    field[i][j] = field[i][j] + local_sum


def draw_right_way(field):
    i = j = N
    if field[1][1] == 0 or field[N][N] == 0:
        return False
    while i != 1 or j != 1:
        field[i][j] = '#'
        if field[i - 1][j] == 0 and field[i][j - 1] == 0:
            return False
        elif field[i - 1][j] == 0:
            j -= 1
        elif field[i][j - 1] == 0:
            i -= 1
        else:
            if field[i - 1][j] < field[i][j - 1]:
                i -= 1
            else:
                j -= 1
    field[i][j] = '#'
    return True


def draw_other_field(field):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if field[i][j] != '#':
                field[i][j] = '-'


if draw_right_way(field):
    draw_other_field(field)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(field[i][j], end='')
        print()
else:
    print('Impossible')
