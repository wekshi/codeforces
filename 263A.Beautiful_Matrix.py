#!/bin/env python3
matrix = []
for i in range(5):
    matrix.append([int(j) for j in input().split()])
    for j in range(5):
        if matrix[i][j] == 1:
            x = i
            y = j
            break
print(abs(x-2)+abs(y-2))
