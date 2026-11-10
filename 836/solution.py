with open("input.txt") as f:
    n = int(f.readline())
    numbers = list(map(int, f.read().split()))[:n]

chosen = sorted(x for x in numbers if x % 2 == 0 and (x >> 6) % 2 == 1)

with open("output.txt", "w") as f:
    f.write(str(len(chosen)) + "\n")
    if chosen:
        f.write(" ".join(map(str, chosen)))
