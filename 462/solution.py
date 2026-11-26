n = int(open("input.txt").read())

answer = n - n // 2 - n // 3 - n // 5 + n // 6 + n // 10 + n // 15 - n // 30

with open("output.txt", "w") as f:
    f.write(str(answer) + "\n")
