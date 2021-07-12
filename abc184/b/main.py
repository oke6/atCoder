#!/usr/bin/env python3
n, x = map(int, input().split())
s = input()

for i, v in enumerate(s):
  if v=="o":
    x += 1
  else:
    x -= 1
    if x < 0:
      x=0

print(x)