with open("input.txt") as f:
    s = f.read().strip()


def contains(s, t):
    pos = 0
    for ch in t:
        pos = s.find(ch, pos)
        if pos == -1:
            return False
        pos += 1
    return True


count = sum(1 for v in range(100, 1000) if contains(s, str(v)))

with open("output.txt", "w") as f:
    f.write(str(count))
