#!/usr/bin/env python3
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diffs = []

for i in range(N):
  diffs.append(abs(A[i]-B[i]))

diffTotal = sum(diffs)

if diffTotal > K:
  print('No')
  exit()

if (diffTotal%2 != K%2):
  print('No')
  exit()

print('Yes')