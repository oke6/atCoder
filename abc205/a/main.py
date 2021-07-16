#!/usr/bin/env python3
a, b = map(int, input().split())

result = a*b/100
if result == int(result):
  print(int(result))
else:
  print(result)
