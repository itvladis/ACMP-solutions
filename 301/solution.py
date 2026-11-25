with open("input.txt") as f:
    s, k = map(int, f.read().split())

rest = s
largest = []
for _ in range(k):
    digit = min(9, rest)
    largest.append(str(digit))
    rest -= digit

rest = s
smallest = []
for _ in range(k - 1):
    digit = min(9, rest - 1)
    smallest.append(str(digit))
    rest -= digit
smallest.append(str(rest))

with open("output.txt", "w") as f:
    f.write("".join(largest) + " " + "".join(reversed(smallest)) + "\n")
