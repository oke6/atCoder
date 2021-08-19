#!/usr/bin/env python3
l, r = map(int, input().split())

lDigits = len(str(l))
rDigits = len(str(r))

ans = 0

for i in range(lDigits, rDigits+1):
  tmpLeft = 10**(i-1)
  tmpRight = 10**(i) - 1

  if i == lDigits:
    tmpLeft = l
  if i == rDigits:
    tmpRight = r
  
  tmpCount = tmpRight - tmpLeft + 1
  
  ans += ((tmpLeft + tmpRight) * tmpCount) * i // 2 % (10**9 + 7)
  ans %= (10**9 + 7)

print(ans)