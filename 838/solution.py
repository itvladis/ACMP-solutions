costs = {' ': 4, '.': 5, ';': 7, ',': 2, '(': 1, ')': 1}
for c in '=+-\'"':
    costs[c] = 3
for c in '{}[]<>':
    costs[c] = 8
for d in range(10):
    costs[str(d)] = 13 - d
for i in range(26):
    letter = chr(ord('a') + i)
    costs[letter] = sum(map(int, str(i + 1)))
    costs[letter.upper()] = costs[letter] + 10

with open('input.txt') as f:
    text = f.read()

total = sum(costs.get(c, 0) for c in text)

with open('output.txt', 'w') as f:
    f.write(str(total))
