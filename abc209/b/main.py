#!/usr/bin/env python3

N, X = map(int, input().split())
list = list(map(int, input().split()))


total = 0

for i, price in enumerate(list):
    if i % 2 == 0:
      total = total + price
    else:
      total = total + price - 1

if total > X:
  print('No')
else:
  print('Yes')