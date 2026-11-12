lines = open("input.txt").read().split("\n")
n, m = map(int, lines[0].split())
rest = [s for s in lines[1:] if s.strip()]
before, after = rest[:n], rest[n:2 * n]


def places(field):
    pos = {}
    for i, row in enumerate(field):
        for j, ch in enumerate(row[:m]):
            if ch != ".":
                pos[ch] = (i, j)
    return pos


a, b = places(before), places(after)
moved = [ch for ch in a if a[ch] != b.get(ch)]
moved.sort(key=lambda ch: (ch.isupper(), ch))
open("output.txt", "w").write(f"{len(moved)}\n{''.join(moved)}\n")
