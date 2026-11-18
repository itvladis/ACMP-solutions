from fractions import Fraction

with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
fortunes = sorted(data[1:1 + n])
money = Fraction(data[1 + n])

for fortune in fortunes:
    if fortune > money:
        money = (money + fortune) / 2

scaled = money * 10 ** 6
rounded = int(scaled + Fraction(1, 2))

with open("output.txt", "w") as f:
    f.write(f"{rounded // 10 ** 6}.{rounded % 10 ** 6:06d}")
