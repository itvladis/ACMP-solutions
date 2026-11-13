with open("input.txt") as f:
    message = f.readline().strip()
    word = f.readline().strip()

answer = "IMPOSSIBLE"
for shift in range(26):
    text = "".join(chr((ord(c) - 65 - shift) % 26 + 65) for c in message)
    if word in text:
        answer = text
        break

with open("output.txt", "w") as f:
    f.write(answer + "\n")
