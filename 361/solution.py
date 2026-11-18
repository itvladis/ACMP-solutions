with open("input.txt") as f:
    s = f.read().strip()

n = len(s)
answer = 0
for length in range(n - 1, 0, -1):
    seen = set()
    found = False
    for start in range(n - length + 1):
        key = "".join(sorted(s[start:start + length]))
        if key in seen:
            found = True
            break
        seen.add(key)
    if found:
        answer = length
        break

with open("output.txt", "w") as f:
    f.write(str(answer))
