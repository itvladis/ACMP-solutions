n = int(open("input.txt").read())
lim = 2 * n
sieve = [True] * (lim + 1)
sieve[0] = sieve[1] = False
for i in range(2, int(lim ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = [False] * len(sieve[i * i::i])
open("output.txt", "w").write(str(sum(sieve[n + 1:lim])))
