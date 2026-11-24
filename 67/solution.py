def to_int(ip):
    value = 0
    for part in ip.split("."):
        value = value * 256 + int(part)
    return value


with open("input.txt") as f:
    tokens = f.read().split()

n = int(tokens[0])
by_length = [0] * 33
for i in range(1, n + 1):
    by_length[bin(to_int(tokens[i])).count("1")] += 1

up_to = [0] * 33
total = 0
for k in range(33):
    total += by_length[k]
    up_to[k] = total

m = int(tokens[n + 1])
lines = []
pos = n + 2
for _ in range(m):
    diff = to_int(tokens[pos]) ^ to_int(tokens[pos + 1])
    pos += 2
    lines.append(str(up_to[32 - diff.bit_length()]))

with open("output.txt", "w") as f:
    f.write("\n".join(lines))
