s = open("input.txt").read().strip()
if s.count(s[0]) == len(s):
    ans = "NO SOLUTION"
elif s != s[::-1]:
    ans = s
else:
    ans = s[:-1]
open("output.txt", "w").write(ans)
