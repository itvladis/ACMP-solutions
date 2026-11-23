import heapq

with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
heap = data[1:n + 1]
heapq.heapify(heap)

total = 0
while len(heap) > 1:
    s = heapq.heappop(heap) + heapq.heappop(heap)
    total += s
    heapq.heappush(heap, s)

cents = total * 5
with open("output.txt", "w") as f:
    f.write(f"{cents // 100}.{cents % 100:02d}")
