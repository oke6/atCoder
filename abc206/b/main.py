#!/usr/bin/env python3
n = int(input()) 

x = 1
while x * (x+1) < 2*n:
  x += 1

print(x)
