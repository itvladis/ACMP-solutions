n, k = map(int, open("input.txt").read().split())
people = list(range(1, n + 1))
i = 0
while len(people) > 1:
    i = (i + k - 1) % len(people)
    people.pop(i)
open("output.txt", "w").write(str(people[0]))
