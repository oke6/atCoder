#!/usr/bin/env python3
n = int(input()) 
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

remA = [0 for _ in range(46)]
remB = [0 for _ in range(46)]
remC = [0 for _ in range(46)]

for i in range(n):
  remA[A[i]%46] += 1
  remB[B[i]%46] += 1
  remC[C[i]%46] += 1

ans = 0
for i in range(46):
  for j in range(46):
    for k in range(46):
      if (i+j+k)%46 == 0:
        ans += remA[i]*remB[j]*remC[k]

print(ans)

