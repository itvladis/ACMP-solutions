with open("input.txt", "rb") as f:
    lines = f.read().split(b"\n")

h = int(lines[0])
order = list(map(int, lines[1].split()))
message = lines[2].strip()

length = len(message)
cols = (length + h - 1) // h
full = length - (cols - 1) * h
sizes = [cols if r < full else cols - 1 for r in range(h)]

rows = [b""] * h
pos = 0
for r in order:
    rows[r - 1] = message[pos:pos + sizes[r - 1]]
    pos += sizes[r - 1]

result = bytearray()
for c in range(cols):
    for r in range(h):
        if c < len(rows[r]):
            result.append(rows[r][c])

with open("output.txt", "wb") as f:
    f.write(bytes(result) + b"\n")
