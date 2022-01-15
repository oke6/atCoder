#!/usr/bin/env python3
n = int(input())

ans = 'A'
nbin = str(bin(n)[2:])

for i in range(1, len(nbin)):
  if nbin[i] == '1':
    ans += 'BA'
  else:
    ans += 'B'

print(ans)
