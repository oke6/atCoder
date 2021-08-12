#!/usr/bin/env python3
from collections import deque
N, Q = map(int, input().split())
A = list(map(int, input().split()))

tmp = 0

for i in range(Q):
  t, x, y = map(int, input().split())
  if t == 1:
    A[(x-tmp)%N - 1], A[(y-tmp)%N - 1] = A[(y-tmp)%N - 1], A[(x-tmp)%N - 1]
  elif t == 2:
    tmp += 1
    if tmp == N:
      tmp = 0
  else:
    print(A[(x-tmp)%N - 1])








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