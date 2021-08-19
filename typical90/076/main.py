#!/usr/bin/env python3
n = int(input()) 
A = list(map(int, input().split()))

sum = sum(A)

tmpSize = A[0]
left = 0
right = 0
for i in range(4*n):
  if tmpSize == sum/10:
    print('Yes')
    exit()
  
  if tmpSize > sum/10:
    tmpSize -= A[left%n]
    left += 1
  else:
    right += 1
    tmpSize += A[right%n]
else:
  print('No')
