#!/usr/bin/env python3

N, Q = map(int, input().split())
A = list(map(int, input().split()))

B = [0 for _ in range(N)]
cost = 0
for i in range(1, N):
  B[i] = (A[i] - A[i-1])
  cost += abs(B[i])

tmpCost = 0
for i in range(Q):
  l, r, v = map(int, input().split())
  if l != 1:
    tmpCost = abs(B[l-1])
    B[l-1] += v
    cost += abs(B[l-1]) - tmpCost
  if r != N:
    tmpCost = abs(B[r])
    B[r] -= v
    cost += abs(B[r]) - tmpCost
  print(cost)