from collections import Counter

with open("input.txt") as f:
    cards = list(map(int, f.read().split()))

counts = sorted(Counter(cards).values(), reverse=True)
values = sorted(cards)

if counts[0] == 5:
    result = "Impossible"
elif counts[0] == 4:
    result = "Four of a Kind"
elif counts == [3, 2]:
    result = "Full House"
elif len(counts) == 5 and values[4] - values[0] == 4:
    result = "Straight"
elif counts[0] == 3:
    result = "Three of a Kind"
elif counts[:2] == [2, 2]:
    result = "Two Pairs"
elif counts[0] == 2:
    result = "One Pair"
else:
    result = "Nothing"

with open("output.txt", "w") as f:
    f.write(result + "\n")
