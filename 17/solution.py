with open('input.txt') as f:
    data = f.read().split()

n = int(data[0])
seq = data[1:n]
length = n - 1

answer = length
for p in range(1, length + 1):
    if length % p == 0 and all(seq[i] == seq[i - p] for i in range(p, length)):
        answer = p
        break

with open('output.txt', 'w') as f:
    f.write(str(answer))
