def options(ch):
    if ch.isdigit():
        return {ch}
    if ch == "?":
        return set("0123456789")
    start = ord(ch) - ord("a")
    return {str(d) for d in range(start, start + 4)}


with open("input.txt") as f:
    p1, p2 = f.read().split()

count = 1
for a, b in zip(p1, p2):
    count *= len(options(a) & options(b))

with open("output.txt", "w") as f:
    f.write(str(count))
