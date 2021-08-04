#!/usr/bin/env python3
a, b = map(int, input().split())

if (a > 0) and (b == 0):
  print('Gold')

if (a == 0) and (b>0):
  print('Silver')

if (0 < a) and (0 < b):
  print('Alloy')

