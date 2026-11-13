with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
a = sorted(data[1:n + 1])
result = a[0::2] + a[1::2][::-1]

with open("output.txt", "w") as f:
    f.write(" ".join(map(str, result)) + "\n")
