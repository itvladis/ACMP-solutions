with open("input.txt") as f:
    n, m = map(int, f.readline().split())
    s = f.readline().strip()

words = {s[i:i + m] for i in range(len(s) - m + 1)}

with open("output.txt", "w") as f:
    f.write(str(len(words)))
