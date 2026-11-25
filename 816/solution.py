with open("input.txt") as f:
    tokens = f.read().split()

m, n, k = int(tokens[0]), int(tokens[1]), int(tokens[2])
sets = [set() for _ in range(n + 1)]
owners = [set() for _ in range(m + 1)]

out = []
pos = 3
for _ in range(k):
    command = tokens[pos]
    if command == "ADD":
        element, number = int(tokens[pos + 1]), int(tokens[pos + 2])
        sets[number].add(element)
        owners[element].add(number)
        pos += 3
    else:
        value = int(tokens[pos + 1])
        items = sets[value] if command == "LISTSET" else owners[value]
        out.append(" ".join(map(str, sorted(items))) if items else "-1")
        pos += 2

with open("output.txt", "w") as f:
    f.write("\n".join(out) + ("\n" if out else ""))
