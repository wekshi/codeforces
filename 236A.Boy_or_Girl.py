#!/bin/env python3
name = list(input())
name.sort()
i = 1
while i < len(name):
    if name[i] == name[i-1]:
        name.pop(i)
    else:
        i += 1
if len(name) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
