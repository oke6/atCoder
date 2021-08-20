#!/usr/bin/env python3
n, l = map(int, input().split())
k = int(input())
A = list(map(int, input().split()))

def isOk(num):
  length = 0
  count = 0
  for i in range(n):
    if i == 0:
      length = A[0]
    else:
      length += A[i] - A[i-1]
    
    if length >= num:
      length = 0
      count += 1
  
  length += l - A[n-1]
  if length >= num:
    length = 0
    count += 1
  
  if count >= k+1:
    return True
  else:
    return False

left = -1
right = l+1
ans = 0
while(right - left > 1):
  mid = left + ((right - left) // 2)
  if isOk(mid):
    left = mid
  else:
    right = mid

print(left)