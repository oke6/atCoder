#!/usr/bin/env python3
n = int(input()) 

ans = 1
for i in range(n):
  A = list(map(int, input().split()))
  ans = (ans * sum(A)) % 1000000007

print(ans)
