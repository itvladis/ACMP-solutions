with open("input.txt") as f:
    a, b, k = map(int, f.read().split())

r = a * pow(10, k - 1, b) % b
digit = r * 10 // b

with open("output.txt", "w") as f:
    f.write(str(digit))
