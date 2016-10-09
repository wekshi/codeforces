#!/bin/env python3
d =[]
for i in range(4):
    d.append(int(input()))
n = int(input())
a = [0] * 100001
i = 1
while d[0] * i <= n or d[1] * i <= n or d[2] * i <= n or d[3] * i <= n:
    for j in range(4):
        if d[j] * i <= n:
            a[d[j] * i] = 1
    i += 1
print(sum(a))
