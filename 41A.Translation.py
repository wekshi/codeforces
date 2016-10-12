#!/bin/env python3
s = input()
t = input()
j = 1
for i in range(len(s)):
    if s[i] != t[-j]:
        print("NO")
        exit()
    j += 1
print("YES")
