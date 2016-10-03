#!/bin/env python3
n = int(input())
s = 0
for i in range(n):
    p = [int(j) for j in input().split()]
    if p[0] + p[1] + p[2] >=2:
        s += 1
print(s)
