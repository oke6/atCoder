#!/usr/bin/env python3
V, T, S, D = map(int, input().split())

s = D/V
if T <= s and s <= S:
  print('No')
else:
  print('Yes')