#!/bin/env python3
nk = [int(i) for i in input().split()]
n = nk[0]
k = nk[1]
a = [int(i) for i in input().split()]
i = 0
flag = 0
if a[i] <= k:
    print(i)
    exit()
while flag == 0:
    if a[i] <= k:
        flag = 1
        continue
    i += 1
print(i)
