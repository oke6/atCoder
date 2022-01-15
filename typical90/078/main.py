#!/usr/bin/env python3
N, M = map(int, input().split())

count = {}
for i in range(M):
  a,b = map(int, input().split())
  larger = max(a, b)
  if (larger in count):
    count[larger] += 1
  else:
    count[larger] = 1

ans = 0
for i in range(1, N+1):
  if i in count:
    if count[i] == 1:
      ans += 1

print(ans)