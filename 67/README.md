# Subnet masks

A subnet mask is an IPv4-style address whose binary form is k ones followed by 32 - k zeros. Two
computers are in the same subnet if their addresses ANDed with the mask are equal. Given N masks
and M pairs of IP addresses, for each pair count how many of the subnets contain both computers.

**Input** (`input.txt`): N, then N masks; then M (0 ≤ M ≤ 10000), then M lines with two IP addresses.
**Output** (`output.txt`): for each pair, the number of subnets containing both addresses, one per line.

Examples: `2` / `255.255.255.255` / `255.255.255.0` / `3` / `192.168.31.1 192.168.31.2` /
`192.168.31.3 192.168.31.4` / `192.168.31.1 192.167.31.2` → `1` / `1` / `0`.

https://acmp.ru/index.asp?main=task&id_task=67
