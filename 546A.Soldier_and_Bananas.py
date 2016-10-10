#!/bin/env python3
k,n,w = (int(i) for i in input().split())
s = ((1 + w) * w // 2) * k - n
if s >= 0:
    print(s)
else:
    print(0)
