#!/bin/env python3
w = int(input())
i = 2
while i < w:
    if (w - i) % 2 == 0:
        print("YES")
        exit();
    i += 2
print("NO")
