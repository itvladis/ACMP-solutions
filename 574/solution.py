with open("input.txt") as f:
    s1 = f.readline().strip()
    s2 = f.readline().strip()

with open("output.txt", "w") as f:
    f.write("YES" if sorted(s1) == sorted(s2) else "NO")
