#!/usr/bin/env python3
n = int(input()) 
A = list(map(int, input().split()))

sortedA = sorted(A)
score = sortedA[len(A)-2]

for i in range(n):
  if A[i] == score:
    print(i+1)
    break
