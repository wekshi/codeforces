#!/bin/env python3
n = int(input())
for i in range(n):
    word = input()
    if len(word) <= 10:
        print(word)
        continue
    print(word[0] + str(len(word)-2) + word[len(word)-1])
