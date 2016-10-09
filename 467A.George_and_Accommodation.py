#!/bin/env python3
n = int(input())
s = 0
for i in range(n):
    p,q = (int(j) for j in input().split())
    if q - p >= 2:
        s += 1
print(s)
