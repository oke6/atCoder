#!/usr/bin/env python3
n = int(input())

if n%2 == 1:
  print('')
  exit()

ans = []
for bit in range(2**n):
  kakko = ''
  tmp = 0
  for i in range(n):
    if (bit >> i) & 1:
      tmp += 1
      kakko = kakko + '('
    else:
      tmp -= 1
      kakko = kakko + ')'
    if tmp < 0:
      break
  if tmp == 0:
    ans.append(kakko)

ans.sort()

for i in ans:
  print(i)
