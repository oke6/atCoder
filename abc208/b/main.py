#!/usr/bin/env python3
import math

p = int(input())
count = 0

for i in reversed(range(1, 11)):
  count = count + (p // math.factorial(i))
  p = p % math.factorial(i)
  if (p == 0):
    break

print(count)

