#!/bin/env python3
nk = [int(i) for i in input().split()]
n = nk[0]
k = nk[1]
a = [int(i) for i in input().split()]
i = 0
flag = 0
while flag == 0 and a[i] != 0:
    if i == k-1:
        flag = 1
        continue
    i += 1
if flag == 1:
    v = a[i]
    while i < n and a[i] == v:
        i += 1
if i == 0 and a[i] == 0:
    print(0)
else:
    print(i)
