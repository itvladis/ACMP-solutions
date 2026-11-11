with open("input.txt") as f:
    lines = f.read().split()

s, t = lines[0], lines[1]
i = 0
for ch in t:
    if i < len(s) and s[i] == ch:
        i += 1

with open("output.txt", "w") as f:
    f.write("YES" if i == len(s) else "NO")
