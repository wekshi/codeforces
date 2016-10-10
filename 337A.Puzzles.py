#!/bin/env python3
n,m = (int(i) for i in input().split())
shop = [int(i) for i in input().split()]
shop.sort()
i = 0
x = 1000
while i <= m - n:
    if shop[i+n-1] - shop[i] < x:
        x = shop[i+n-1] - shop[i]
    i += 1
print(x)
