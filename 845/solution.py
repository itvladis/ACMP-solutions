x, y = map(int, open("input.txt").read().split())

with open("output.txt", "w") as f:
    f.write(str(pow(x, y, 10)) + "\n")
