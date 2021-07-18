#!/usr/bin/env python3
a, b, c = map(int, input().split())

if a == b:
  print('=')
  exit()

if (abs(a) == abs(b)) and (c%2 == 0):
  print('=')
  exit()

if (c%2 == 1):
  if (a > b):
    print('>')
  else:
    print('<')
  exit()

if (c%2 == 0):
  if (abs(a) > abs(b)):
    print('>')
  else:
    print('<')
  exit()

