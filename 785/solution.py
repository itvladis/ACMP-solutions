with open("input.txt") as f:
    a, b = map(int, f.read().split())

result = []
for x in range(a, b + 1):
    if x * x % 10 ** len(str(x)) == x:
        result.append(str(x))

with open("output.txt", "w") as f:
    f.write(" ".join(result))
