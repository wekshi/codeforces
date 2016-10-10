#!/bin/env python3
n,t = (int(i) for i in input().split())
queue = list(input())
for i in range(t):
    j = 0
    while j+1 < n:
        if queue[j] == "B" and queue[j+1] == "G":
            queue[j],queue[j+1] = queue[j+1],queue[j]
            j += 1
        j += 1
for i in queue:
    print(i,end='')
print()
