#!/usr/bin/env python3
from bisect import bisect_left

N = int(input()) 
A = list(map(int, input().split()))
Q = int(input())

A.sort()

for i in range(Q):
  b = int(input())
  pos = bisect_left(A, b)
  
  if pos == 0:
    print(abs(A[0] - b))
    continue
  if pos == N:
    print(abs(A[-1] - b))
    continue

  if (abs(A[pos] - b)) > (abs(A[pos-1] - b)):
    print(abs(A[pos-1] - b))
  else:
    print(abs(A[pos] - b))

