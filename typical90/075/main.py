#!/usr/bin/env python3
N = int(input())

num = int(pow(N, 0.5))

res = 0
for i in range(2,num+1):
  while N % i == 0:
    N = N // i
    res += 1
else:
  if N != 1:
    res += 1

ans = 0
tmp = 1
while tmp < res:
  tmp *= 2
  ans += 1

print(ans) 

