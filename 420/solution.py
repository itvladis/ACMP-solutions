s = open("input.txt").read().strip()


def valid(s):
    i = 0
    prev = None
    while i < len(s):
        if not s[i].isupper():
            return False
        j = i + 1
        if j < len(s) and s[j].islower():
            j += 1
        element = s[i:j]
        k = j
        while k < len(s) and s[k].isdigit():
            k += 1
        count = s[j:k]
        if count and (count[0] == "0" or int(count) < 2):
            return False
        if element == prev:
            return False
        prev = element
        i = k
    return True


with open("output.txt", "w") as f:
    f.write("YES\n" if s and valid(s) else "NO\n")
