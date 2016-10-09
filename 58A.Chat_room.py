#!/bin/env python3
import re
hello = "hello"
str = input()
pattern = re.compile(r".*h.*e.*l.*l.*o.*")
match = pattern.match(str)
if match:
    print("YES")
else:
    print("NO")
