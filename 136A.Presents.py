#!/bin/env python3
n = int(input())
f = [int(i)-1 for i in input().split()]
r = [0] * n
for i in range(n):
    r[f[i]] = i
for i in range(n):
    print(r[i]+1,end='')
    if i != n-1:
        print(" ",end='')
print()
