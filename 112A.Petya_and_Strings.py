#!/bin/env python3
str1 = input().lower()
str2 = input().lower()
flag = 0
for i in range(len(str1)):
    if str1[i] > str2[i]:
        flag = 1
        break
    if str1[i] < str2[i]:
        flag = -1
        break
print(flag)
