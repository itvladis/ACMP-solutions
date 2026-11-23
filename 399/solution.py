from collections import deque


def main():
    with open("input.txt") as f:
        lines = f.read().split("\n")
    n, m = map(int, lines[0].split())
    grid = [lines[i + 1].rstrip("\r").ljust(m)[:m] for i in range(n)]
    start = (1, 1)
    finish = (n - 2, m - 2)
    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

    seen = [[False] * m for _ in range(n)]
    seen[1][1] = True
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if grid[nr][nc] != "@" and not seen[nr][nc]:
                seen[nr][nc] = True
                queue.append((nr, nc))
    if not seen[finish[0]][finish[1]]:
        with open("output.txt", "w") as f:
            f.write("-1")
        return

    visits = [[0] * m for _ in range(n)]
    visits[1][1] = 1
    r, c = start
    direction = -1
    steps = 0
    while (r, c) != finish:
        best = None
        options = []
        for d, (dr, dc) in enumerate(moves):
            nr, nc = r + dr, c + dc
            if grid[nr][nc] == "@":
                continue
            v = visits[nr][nc]
            if best is None or v < best:
                best = v
                options = [d]
            elif v == best:
                options.append(d)
        d = direction if direction in options else options[0]
        direction = d
        r += moves[d][0]
        c += moves[d][1]
        visits[r][c] += 1
        steps += 1

    with open("output.txt", "w") as f:
        f.write(str(steps))


main()
