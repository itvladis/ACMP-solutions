def sec(t):
    h, m, s = map(int, t.split(":"))
    return h * 3600 + m * 60 + s


start, end = map(sec, open("input.txt").read().split())
cnt = [0] * 10
for t in range(start, end + 1):
    for ch in f"{t // 3600:02}{t // 60 % 60:02}{t % 60:02}":
        cnt[int(ch)] += 1
open("output.txt", "w").write("\n".join(map(str, cnt)))
