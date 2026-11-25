with open("input.txt") as f:
    n = int(f.read())

lowest = n & -n
ripple = n + lowest
answer = ripple | (((n ^ ripple) >> 2) // lowest)

with open("output.txt", "w") as f:
    f.write(f"{answer}\n")
