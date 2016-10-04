#!/bin/env python3
n = int(input())
a = [int(i) for i in input().split()]
n1 = a.count(1)
n2 = a.count(2)
n3 = a.count(3)
taxi = a.count(4)
if n3 > 0:
    taxi += n3
    if n1 > n3:
        n1 -= n3
    else:
        n1 = 0
if n2 > 0:
    if n1 != 0:
        tmp = n1 // 2 + n1 % 2
        if n2 >= tmp:
            taxi += tmp
            n2 -= tmp
            n1 = 0
        else:
            taxi += n2
            n1 -= n2 * 2
            n2 = 0
    taxi += n2 // 2 + n2 % 2
taxi += n1 // 4
if n1 % 4:
    taxi += 1
print(taxi)
