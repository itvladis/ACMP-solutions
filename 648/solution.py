data = open("input.txt").read().split()
n = int(data[0])
cards = sorted(map(int, data[1:n + 1]))
half = n // 2
open("output.txt", "w").write(str(sum(cards[half:]) - sum(cards[:half])) + "\n")
