KEY = 'the quick brown fox jumps over the lazy dog'


def build_key(line):
    if len(line) != len(KEY):
        return None
    mapping = {}
    used = {}
    for c, p in zip(line, KEY):
        if (c == ' ') != (p == ' '):
            return None
        if c == ' ':
            continue
        if mapping.get(c, p) != p or used.get(p, c) != c:
            return None
        mapping[c] = p
        used[p] = c
    return mapping


with open('input.txt') as f:
    lines = f.read().split('\n')

n = int(lines[0])
letter = [line.rstrip('\r') for line in lines[1:n + 1]]

mapping = None
for line in letter:
    mapping = build_key(line)
    if mapping:
        break

with open('output.txt', 'w') as f:
    if mapping is None:
        f.write('No solution')
    else:
        f.write('\n'.join(''.join(mapping.get(c, c) for c in line) for line in letter))
