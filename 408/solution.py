with open("input.txt", "rb") as f:
    lines = f.read().replace(b"\r", b"").split(b"\n")

k, n = map(int, lines[0].split())
text = [line.strip(b" ") for line in lines[1:1 + n]]

if any(len(line) > k for line in text):
    result = b"Impossible."
else:
    formatted = []
    for line in text:
        free = k - len(line)
        left = free // 2
        formatted.append(b" " * left + line + b" " * (free - left))
    result = b"\n".join(formatted)

with open("output.txt", "wb") as f:
    f.write(result)
