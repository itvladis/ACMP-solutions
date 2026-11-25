with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n, m = data[0], data[1]
teams = [tuple(data[2 + 3 * i: 5 + 3 * i]) for i in range(n + m)]
basic = teams[:n]
advanced = teams[n:]

result = [team_id for team_id, solved, _ in advanced if solved > 0]

ranked = sorted((t for t in basic if t[1] > 0), key=lambda t: (-t[1], t[2]))
if ranked:
    best = ranked[0][1]
    k = len(ranked)
    median = ranked[k // 2 - 1][1] if k // 2 >= 1 else None
    for team_id, solved, _ in ranked:
        if solved == best or (median is not None and solved > median):
            result.append(team_id)

result.sort()
with open("output.txt", "w") as f:
    f.write(f"{len(result)}\n")
    f.write(" ".join(map(str, result)) + "\n")
