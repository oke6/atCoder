#!/usr/bin/env python3









"""
from collections import deque
N, Q = map(int, input().split())
A = list(map(int, input().split()))

d = deque(A)

for i in range(Q):
  t, x, y = map(int, input().split())
  if t == 1:
    d[x-1], d[y-1] = d[y-1], d[x-1]
  elif t == 2:
    d.rotate()
  else:
    print(d[x-1])
"""