with open('input.txt') as f:
    x0, y0, vx, vy, v, t, d = map(int, f.read().split())

tx = x0 + vx * t
ty = y0 + vy * t
dist2 = tx * tx + ty * ty
r = v * t

ok = dist2 <= (d + r) ** 2 and (d <= r or dist2 >= (d - r) ** 2)

with open('output.txt', 'w') as f:
    f.write('YES' if ok else 'NO')
