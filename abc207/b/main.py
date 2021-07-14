#!/usr/bin/env python3
a, b, c, d = map(int, input().split())

if b >= (d*c):
  print(-1)
else:
  x = a // (c*d-b)
  if (a % (c*d-b) != 0):
    x += 1
  print(x)

