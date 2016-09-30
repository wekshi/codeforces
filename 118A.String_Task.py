#!/bin/env python3
demo = "aoyeui"
line = input()
line = line.lower()
a = list(line)
for i in range(len(a)):
    if demo.find(a[i]) != -1:
        continue
    print('.' + a[i],end='')
print()
