s = open("input.txt").read().strip()
order = sorted(range(26), key=lambda i: s[i])
if all(s[child] >= chr(ord("A") + pos) for pos, child in enumerate(order)):
    result = "YES\n" + " ".join(str(c + 1) for c in order) + "\n"
else:
    result = "NO\n"
open("output.txt", "w").write(result)
