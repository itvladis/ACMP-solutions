with open("input.txt") as f:
    a = list(map(int, f.read().split()))

answer = max(a[1::2]) + min(a[0::2])

with open("output.txt", "w") as f:
    f.write(str(answer))
