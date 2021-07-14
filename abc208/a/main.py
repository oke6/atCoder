#!/usr/bin/env python3
a, b = map(int, input().split())

if 6*a < b or b < a:
  print('No')
else:
  print('Yes')


