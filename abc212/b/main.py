#!/usr/bin/env python3
s = input()

isWeak = False

if (int(s) % 1111 == 0):
  isWeak = True

x1 = int(s[0])
x2 = int(s[1])
x3 = int(s[2])
x4 = int(s[3])

if x2 == ((x1 + 1) % 10):
  if x3 == ((x2 + 1) % 10):
    if x4 == ((x3 + 1) % 10):
      isWeak = True

if isWeak:
  print('Weak')
else:
  print('Strong')



