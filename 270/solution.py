import re

with open("input.txt") as f:
    name = f.read().strip()

if re.fullmatch(r"[a-z]+(_[a-z]+)*", name):
    parts = name.split("_")
    result = parts[0] + "".join(p.capitalize() for p in parts[1:])
elif re.fullmatch(r"[a-z][a-zA-Z]*", name):
    result = "".join("_" + c.lower() if c.isupper() else c for c in name)
else:
    result = "Error!"

with open("output.txt", "w") as f:
    f.write(result)
