with open("input.txt") as f:
    n, w, d, p = map(int, f.read().split())

missing = w * n * (n - 1) // 2 - p
basket = missing // d if missing else n

with open("output.txt", "w") as f:
    f.write(str(basket))
