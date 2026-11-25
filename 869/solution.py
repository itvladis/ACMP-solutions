with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n, d = data[0], data[1]
weights = sorted(data[2:2 + n])

left, right = 0, n - 1
boats = 0
while left <= right:
    if left < right and weights[left] + weights[right] <= d:
        left += 1
    right -= 1
    boats += 1

with open("output.txt", "w") as f:
    f.write(f"{boats}\n")
