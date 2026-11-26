x, m, length, v = map(int, open("input.txt").read().split())

coef = [pow(x, i, m) for i in range(length)]
reach = [[False] * m for _ in range(length + 1)]
choice = [[-1] * m for _ in range(length + 1)]
reach[0][0] = True
for i in range(length):
    for r in range(m):
        if reach[i][r]:
            for digit in range(10):
                nr = (r + digit * coef[i]) % m
                if not reach[i + 1][nr]:
                    reach[i + 1][nr] = True
                    choice[i + 1][nr] = digit

if not reach[length][v % m]:
    answer = "NO SOLUTION"
else:
    digits = []
    r = v % m
    for i in range(length, 0, -1):
        digit = choice[i][r]
        digits.append(str(digit))
        r = (r - digit * coef[i - 1]) % m
    answer = "".join(reversed(digits))

with open("output.txt", "w") as f:
    f.write(answer + "\n")
