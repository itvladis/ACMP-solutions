import re

with open('input.txt') as f:
    lines = f.read().splitlines()

n = int(lines[0])
best_name = None
best_time = None
for line in lines[1:n + 1]:
    m = re.match(r'\s*(".*")\s+(\d+):(\d+)\s+(\d+):(\d+)\s*$', line)
    name = m.group(1)
    dep = int(m.group(2)) * 60 + int(m.group(3))
    arr = int(m.group(4)) * 60 + int(m.group(5))
    duration = (arr - dep) % 1440
    if duration == 0:
        duration = 1440
    if best_time is None or duration < best_time:
        best_time = duration
        best_name = name

speed = (650 * 60 * 2 + best_time) // (2 * best_time)

with open('output.txt', 'w') as f:
    f.write(f'The fastest train is {best_name}.\n')
    f.write(f'Its speed is {speed} km/h, approximately.\n')
