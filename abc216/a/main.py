#!/usr/bin/env python3

n = float(input())
x = int(n)
y = int((n - x)*10)

if 0 <= y and y<= 2:
  print(str(x) + '-')
elif 3 <= y and y<= 6:
  print(str(x))
else:
  print(str(x) + '+')