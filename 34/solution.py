with open("input.txt") as f:
    n, k = map(int, f.readline().split())
    code = f.readline().strip()

seen = set()
found = False
for i in range(len(code) - k + 1):
    part = code[i:i + k]
    if part in seen:
        found = True
        break
    seen.add(part)

with open("output.txt", "w") as f:
    f.write("YES\n" if found else "NO\n")
