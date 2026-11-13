import re

with open("input.txt") as f:
    data = f.read().split()

n = int(data[0])
answers = []
for word in data[1:n + 1]:
    m = re.fullmatch(r"(0+)(1+)(2+)", word)
    ok = m is not None and len(m.group(1)) == len(m.group(2)) == len(m.group(3))
    answers.append("YES" if ok else "NO")

with open("output.txt", "w") as f:
    f.write("\n".join(answers) + "\n")
