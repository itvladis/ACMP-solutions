with open("input.txt") as f:
    start, finish = f.read().split()

dx = abs(ord(finish[0]) - ord(start[0]))
dy = int(finish[1]) - int(start[1])
ok = dy > 0 and dx <= dy and (dy - dx) % 2 == 0

with open("output.txt", "w") as f:
    f.write("YES" if ok else "NO")
