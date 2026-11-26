with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

ip = lines[0].split()[1]
times = []
for line in lines[1:5]:
    if line.startswith("Reply"):
        times.append(int(line.split("Time=")[1]))

received = len(times)
lost = 4 - received
out = [
    f"Ping statistics for {ip}:",
    f"Packets: Sent = 4 Received = {received} Lost = {lost} ({lost * 25}% loss)",
]
if received:
    avg = (2 * sum(times) + received) // (2 * received)
    out.append("Approximate round trip times:")
    out.append(f"Minimum = {min(times)} Maximum = {max(times)} Average = {avg}")

with open("output.txt", "w") as f:
    f.write("\n".join(out) + "\n")
