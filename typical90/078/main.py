#!/usr/bin/env python3
n, m = map(int, input().split())

tops = {}
count = 0
for i in range(m):
  a, b = map(int, input().split())
  large = max(a, b)
  if large in tops:
    tops[large] += 1
  else:
    tops[large] = 1

for v in tops.values():
  if v == 1:
    count += 1

print(count)

