#!/usr/bin/env python3

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = 0
for i in range(N):
  diff += abs(A[i] - B[i])

if diff > K:
  print('No')
  exit()

if (diff % 2) == (K % 2):
  print('Yes')
else:
  print('No')