with open('input.txt') as f:
    lines = f.read().split()

s, t = lines[0], lines[1]
n = len(s)
pos = (s + s).rfind(t, 1, 2 * n)
answer = n - pos if pos != -1 else -1

with open('output.txt', 'w') as f:
    f.write(str(answer))
