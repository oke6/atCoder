#!/usr/bin/env python3
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

x = r2-r1
y = c2-c1

if r1 == r2 and c1 == c2:
  print(0)
  exit()

if ((r1 + c1) == (r2 + c2)) or ((r1 - c1) == (r2 - c2)) or ((abs(x) + abs(y)) <= 3):
  print(1)
  exit()

if (abs(x)%2 == abs(y)%2):
  print(2)
  exit()

if (abs(x-y) <= 3 or abs(x+y) <= 3):
  print(2)
  exit()

print(3)



