with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
a = data[1:n + 1]

suffix = [0] * n
suffix[-1] = a[-1]
for i in range(n - 2, -1, -1):
    suffix[i] = max(a[i], suffix[i + 1])

result = []
left = a[0]
for i in range(n):
    left = max(left, a[i])
    right = suffix[i]
    if a[i] >= left or a[i] >= right:
        result.append(a[i])

with open("output.txt", "w") as f:
    f.write(f"{len(result)}\n{' '.join(map(str, result))}")
