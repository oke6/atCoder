#!/usr/bin/env python3
a, b = map(int, input().split())
count = 0;

for i in range(101):
  if i >= a and i <= b:
    count = count + 1;

print(count);
