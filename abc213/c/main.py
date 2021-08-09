#!/usr/bin/env python3
from bisect import bisect_left

H, W, N = map(int,input().split())
A, B = [], []
for i in range(N):
  a, b=map(int, input().split())
  A.append(a)
  B.append(b)

X = list(set(A))
X.sort()
Y = list(set(B))
Y.sort()

for i in range(N):
  c = bisect_left(X, A[i]) + 1
  d = bisect_left(Y, B[i]) + 1
  print(c, d)

#Xdict = {x:i+1 for i,x in enumerate(sorted(list(set(X))))}
#Ydict = {y:i+1 for i,y in enumerate(sorted(list(set(Y))))}