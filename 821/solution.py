with open("input.txt") as f:
    n = int(f.readline())
    moves = f.readline().strip()

board = [[i * n + j + 1 for j in range(n)] for i in range(n)]
board[n - 1][n - 1] = 0
r = c = n - 1
shift = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

error = 0
for step, move in enumerate(moves, 1):
    dr, dc = shift[move]
    nr, nc = r + dr, c + dc
    if not (0 <= nr < n and 0 <= nc < n):
        error = step
        break
    board[r][c], board[nr][nc] = board[nr][nc], 0
    r, c = nr, nc

with open("output.txt", "w") as f:
    if error:
        f.write(f"ERROR {error}\n")
    else:
        f.write("\n".join(" ".join(map(str, row)) for row in board) + "\n")
