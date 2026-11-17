with open('input.txt') as f:
    data = f.read().split()

n = int(data[0])
notes = sorted(set(data[1:n + 1]))

count = 0
for i, word in enumerate(notes):
    if i + 1 == len(notes) or not notes[i + 1].startswith(word):
        count += 1

with open('output.txt', 'w') as f:
    f.write(str(count))
