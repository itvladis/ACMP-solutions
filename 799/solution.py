with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
a = data[1:n + 1]
top = max(a)
first = a.index(top)

best = -1
for i in range(first + 1, n - 1):
    if a[i] % 10 == 5 and a[i + 1] < a[i]:
        best = max(best, a[i])

place = 0
if best != -1:
    place = sum(1 for x in a if x > best) + 1

with open("output.txt", "w") as f:
    f.write(str(place))
