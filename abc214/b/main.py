#!/usr/bin/env python3
s, t = map(int, input().split())

ans = 0
for i in range(s+1):
  for j in range(s+1):
    for k in range(s+1):
      if (i+j+k <= s) and i*j*k <=t:
        ans += 1

print(ans)
