#!/usr/bin/env python3
N, K = map(int, input().split())

def base8to10(base8):
  base10 = 0
  for i in range(len(str(base8))):
    base10 += int(str(base8)[-(i+1)]) * 8**(i)
  return base10

def base10to9(base10):
  if base10 == 0:
    return 0
  
  base9 = ''
  while(base10 > 0):
    base10, mod = divmod(base10, 9)
    base9 = str(mod) + base9
  return int(base9)

def proc(before):
  num = base10to9(base8to10(before))
  replaced = str(num).replace('8', '5')
  return int(replaced)

ans = N
for i in range(K):
  ans = proc(ans)

print(ans)


