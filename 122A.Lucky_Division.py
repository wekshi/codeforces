#!/bin/env python3
n = int(input())
luck = [4,7,47,74,474,477,744,747,774,777]
flag = [i for i in luck if n % i == 0]
if flag:
    print("YES")
else:
    print("NO")
