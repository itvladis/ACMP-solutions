with open("input.txt") as f:
    n = int(f.readline())
    items = [f.readline().split() for _ in range(n)]

signs = [s for s, _ in items]
amounts = [int(a) for _, a in items]
total = sum(amounts)

result = [100 * a // total for a in amounts]
left = 100 - sum(result)
fractional = [i for i in range(n) if 100 * amounts[i] % total]
order = [i for i in fractional if signs[i] == "+"] + [i for i in fractional if signs[i] == "-"]
for i in order[:left]:
    result[i] += 1

with open("output.txt", "w") as f:
    f.write("\n".join(map(str, result)) + "\n")
