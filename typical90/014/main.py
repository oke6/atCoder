#!/usr/bin/env python3
n = int(input()) 
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

count = 0
for i in range(n):
  count += abs(A[i] - B[i])

print(count)