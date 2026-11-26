# Packet exchange

A `ping` command sends 4 packets to a server; each one either times out or comes back
after some number of milliseconds. Given the log of the four packets, print the ping
statistics: how many packets were received and lost (with the loss percentage), and the
minimum, maximum and average round trip time (the average is rounded half up). If every
packet was lost, only the first two lines of the statistics are printed.

**Input** (`input.txt`): the line `ping IP`, then 4 lines, each either `Time out` or `Reply from IP Time=t`.
**Output** (`output.txt`): the statistics block in the format shown in the example.

Examples: `ping 209.85.135.147` / `Time out` / `Time=100` / `Time=300` / `Time=200` → `Ping statistics for 209.85.135.147:` / `Packets: Sent = 4 Received = 3 Lost = 1 (25% loss)` / `Approximate round trip times:` / `Minimum = 100 Maximum = 300 Average = 200`.

https://acmp.ru/index.asp?main=task&id_task=987
