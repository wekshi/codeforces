#!/bin/env python3
n = int(input())
coins = [int(i) for i in input().split()]
coins.sort(reverse = True)
s = sum(coins)
my = 0
for i in range(len(coins)):
    my += coins[i]
    if my > s - my:
        print(i+1)
        break
