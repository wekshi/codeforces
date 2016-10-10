#!/bin/env python3
y = int(input()) + 1
while True:
    a = y // 1000
    b = y % 1000 // 100
    c = y % 100 // 10
    d = y % 10
    if  ( a != b and a != c and a != d and
          b != c and b != d and
          c != d ):
        print(y)
        break
    y += 1
