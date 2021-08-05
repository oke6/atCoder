#!/usr/bin/env python3
H, W = map(int, input().split())
A = []
for i in range(H):
  array = list(map(int, input().split()))
  A.append(array)

rowSum = []
for i in range(H):
  tmp = 0
  for j in range(W):
      tmp += A[i][j]
  rowSum.append(tmp)

colSum = []
for j in range(W):
  tmp = 0
  for i in range(H):
    tmp += A[i][j]
  colSum.append(tmp)

for i in range(H):
  B = []
  for j in range(W):
    B.append(str(rowSum[i] + colSum[j] - A[i][j]))
  #ans = " ".join(B)
  print(*B)

