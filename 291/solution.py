from collections import Counter

with open('input.txt') as f:
    lines = f.read().split()

n = int(lines[0])
words = lines[1:n + 1]
letters = Counter(lines[n + 1])

count = 0
for word in words:
    need = Counter(word)
    if all(letters[c] >= v for c, v in need.items()):
        count += 1

with open('output.txt', 'w') as f:
    f.write(str(count))
