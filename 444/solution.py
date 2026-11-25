with open("input.txt") as f:
    data = f.read().split()

n = int(data[0])
nums = sorted(set(map(int, data[1:1 + n])))
count = len(nums)

best = [0] + [None] * count
parts = [None] * (count + 1)
for i in range(1, count + 1):
    j = i - 1
    while j >= 0 and (j == i - 1 or nums[j] + 1 == nums[j + 1]):
        piece = str(nums[j]) if j == i - 1 else f"{nums[j]}, ..., {nums[i - 1]}"
        cost = best[j] + len(piece) + (2 if j > 0 else 0)
        if best[i] is None or cost < best[i]:
            best[i] = cost
            parts[i] = (j, piece)
        j -= 1

pieces = []
i = count
while i > 0:
    j, piece = parts[i]
    pieces.append(piece)
    i = j

with open("output.txt", "w") as f:
    f.write(", ".join(reversed(pieces)) + "\n")
