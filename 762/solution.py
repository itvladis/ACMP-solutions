with open("input.txt") as f:
    n = int(f.read())

count = 0
reach = 1
while reach < n:
    reach *= 3
    count += 1

with open("output.txt", "w") as f:
    f.write(str(count) + "\n")
