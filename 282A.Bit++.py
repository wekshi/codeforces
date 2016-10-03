#!/bin/env pyhton3
n = int(input())
s = 0
for i in range(n):
    p = input()
    if p.find('+') == -1:
        s -= 1
    else:
        s += 1
print(s)
