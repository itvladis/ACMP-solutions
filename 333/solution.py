with open("input.txt") as f:
    a, b, c = f.read().split()

common = sorted(set(a) & set(b) & set(c))

with open("output.txt", "w") as f:
    f.write(str(len(common)) + "\n")
    if common:
        f.write(" ".join(common) + "\n")
