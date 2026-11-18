with open("input.txt") as f:
    w, h = map(int, f.read().split()[:2])

with open("output.txt", "w") as f:
    f.write(str(w * (w + 1) // 2 * (h * (h + 1) // 2)))
