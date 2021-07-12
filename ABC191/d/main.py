#!/usr/bin/env python3
X, Y, R = map(float, input().split())

count=0
val = (10 ** 5) + 1
for x in range((10 ** 5) + 1):
  for y in range((10 ** 5) + 1):
    if (x-X)**2 + (y-Y)**2 <= R**2:
      count+=1

print(count)
