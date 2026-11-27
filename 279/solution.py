with open('input.txt') as f:
    s = f.read().strip()

stack = []
cost = 0
ok = True
for ch in s:
    if ch in '([':
        stack.append(ch)
    else:
        if not stack:
            ok = False
            break
        top = stack.pop()
        if (top == '(') != (ch == ')'):
            cost += 1

if stack:
    ok = False

with open('output.txt', 'w') as f:
    f.write(str(cost) if ok else '-1')
