#!/usr/bin/env python3
n = int(input()) 
s = input()

prev = s[0]
num = 1
blocks = []
for i in range(1, n):
  if prev != s[i]:
    blocks.append(num)
    num = 1
    prev = s[i]
  else:
    num += 1
else:
  blocks.append(num)

notCount = 0
for block in blocks:
  notCount += block*(block+1)//2

ans = n*(n+1)//2 - notCount
print(ans)