n = int(open("input.txt").read())
regions = 1 if n == 0 else n * n - n + 2
open("output.txt", "w").write(str(regions) + "\n")
