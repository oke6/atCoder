#!/usr/bin/env python3
n, y = map(int, input().split())

for i in range(n+1):
  for j in range(n+1-i):
    if i*10000+j*5000+(n-i-j)*1000 == y:
      print(str(i) + " " + str(j) + " " + str(n-i-j))
      break
  else:
    continue
  break
else:
  print("-1 -1 -1")


