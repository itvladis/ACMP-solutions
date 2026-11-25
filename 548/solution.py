with open("input.txt") as f:
    a = f.readline().strip()
    b = f.readline().strip()

i = j = 0
result = []
while i < len(a) or j < len(b):
    if a[i:] + ":" <= b[j:] + ":":
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

with open("output.txt", "w") as f:
    f.write("".join(result) + "\n")
