with open("input.txt") as f:
    m, n = map(int, f.read().split())

sieve = bytearray([1]) * (n + 1)
sieve[0] = sieve[1] = 0
i = 2
while i * i <= n:
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    i += 1

primes = [str(p) for p in range(m, n + 1) if sieve[p]]

with open("output.txt", "w") as f:
    f.write("\n".join(primes) if primes else "Absent")
