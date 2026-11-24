with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
people = [(data[2 + 2 * i], data[1 + 2 * i], i) for i in range(n)]
people.sort()

finish = [0] * n
latest = 0
for steps, speed, index in people:
    latest = max(latest, steps * speed)
    finish[index] = latest

with open("output.txt", "w") as f:
    f.write("\n".join(map(str, finish)))
