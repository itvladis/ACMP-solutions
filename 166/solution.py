def newborn(count):
    best = 0
    fives = count // 5
    for b in range(max(0, fives - 4), fives + 1):
        a = (count - 5 * b) // 3
        best = max(best, 5 * a + 9 * b)
    return best


with open('input.txt') as f:
    k, n = map(int, f.read().split())

ages = [k, 0, 0]
for _ in range(n - 1):
    born = newborn(sum(ages))
    ages = [born, ages[0], ages[1]]

with open('output.txt', 'w') as f:
    f.write(str(sum(ages)))
