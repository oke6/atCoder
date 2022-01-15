#!/usr/bin/env python3
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A.sort()

for i in range(Q):
  b = int(input())
  index = bisect_left(A, b)
  if index == 0:
    ans = abs(A[index]-b)
  elif index == len(A):
    ans = abs(A[index-1]-b)
  else:
    ans = min(abs(A[index-1]-b), abs(A[index]-b))
  print(ans)

