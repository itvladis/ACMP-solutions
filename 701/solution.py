age, prize = open("input.txt").read().split()
base = int(age) % 10 + 2
open("output.txt", "w").write(str(int(prize, base)) + "\n")
