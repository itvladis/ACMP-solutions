with open('input.txt') as f:
    lines = f.read().split()

n, m = int(lines[0]), int(lines[1])
board = lines[2:2 + n]

wrong = [[], []]
for i in range(n):
    for j in range(m):
        expected = 'W' if (i + j) % 2 == 0 else 'B'
        if board[i][j] != expected:
            wrong[0].append((i + 1, j + 1))
        else:
            wrong[1].append((i + 1, j + 1))

cells = wrong[0] if len(wrong[0]) <= len(wrong[1]) else wrong[1]

with open('output.txt', 'w') as f:
    f.write(str(len(cells)) + '\n')
    for i, j in cells:
        f.write(f'{i} {j}\n')
