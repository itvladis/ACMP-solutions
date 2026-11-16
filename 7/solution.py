with open('input.txt') as f:
    piles = list(map(int, f.read().split()))

with open('output.txt', 'w') as f:
    f.write(str(max(piles)))
