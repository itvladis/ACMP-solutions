def prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


d = sorted(open("input.txt").read().strip())
up = int("".join(d))
down = int("".join(reversed(d)))
open("output.txt", "w").write("Yes" if prime(up) and prime(down) else "No")
