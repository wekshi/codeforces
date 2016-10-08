#!/bin/env python3
n = int(input())
str = list(input())
for i in range(n):
    team = []
    for j in range(len(str)-1):
        if str[j] == str[j+1]:
            team.append(j)
    if team == []:
        break
    team.reverse()
    for j in team:
        str.pop(j)
print(n - len(str))
