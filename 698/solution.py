ranks = "6789TJQKA"

with open("input.txt") as f:
    n, m, trump = f.readline().split()
    hand = f.readline().split()
    attack = f.readline().split()


def beats(card, target):
    if card[1] == target[1]:
        return ranks.index(card[0]) > ranks.index(target[0])
    return card[1] == trump


owner = [-1] * len(hand)


def assign(t, seen):
    for c in range(len(hand)):
        if c not in seen and beats(hand[c], attack[t]):
            seen.add(c)
            if owner[c] == -1 or assign(owner[c], seen):
                owner[c] = t
                return True
    return False


ok = all(assign(t, set()) for t in range(len(attack)))

with open("output.txt", "w") as f:
    f.write("YES\n" if ok else "NO\n")
