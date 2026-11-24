with open("input.txt") as f:
    data = list(map(int, f.read().split()))

k = data[0]
answers = []
for i in range(k):
    n, m = data[1 + 2 * i], data[2 + 2 * i]
    if n >= 2 and m <= (n - 1) * (n - 2) // 2:
        answers.append("Yes")
    else:
        answers.append("No")

with open("output.txt", "w") as f:
    f.write("\n".join(answers))
