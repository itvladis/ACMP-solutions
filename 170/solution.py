with open("input.txt") as f:
    n = int(f.read())

best = 1
k = 1
while k * (k + 1) // 2 <= n:
    if (n - k * (k - 1) // 2) % k == 0:
        best = k
    k += 1

with open("output.txt", "w") as f:
    f.write(str(best))
