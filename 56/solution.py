with open("input.txt") as f:
    lines = [line.strip() for line in f]

n = int(lines[0])
friends = set(lines[1:1 + n])
m = int(lines[1 + n])
friend_of = set(lines[2 + n:2 + n + m])

mutual = friends & friend_of
also = friend_of - friends


def show(title, names):
    return (title + " " + ", ".join(sorted(names))).rstrip()


with open("output.txt", "w") as f:
    f.write(show("Friends:", friends) + "\n")
    f.write(show("Mutual Friends:", mutual) + "\n")
    f.write(show("Also Friend of:", also) + "\n")
