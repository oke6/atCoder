#!/usr/bin/env python3
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = float('inf')
A.sort()
B.sort()

i, j = 0, 0

while(i < len(A) and j < len(B)):
  if A[i] == B[j]:
    result = 0
    break

  if A[i] > B[j]:
    result = min(result, abs(A[i] - B[j]))
    if j == (len(B) - 1):
      i += 1
    else:
      j += 1
  else:
    result = min(result, abs(A[i] - B[j]))
    if i == (len(A) - 1):
      j += 1
    else:
      i += 1

print(result)