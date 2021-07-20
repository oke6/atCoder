#!/usr/bin/env python3
n = int(input()) 
list = list(map(int, input().split()))

result = 0
for i in range(n):
  if list[i] > 10:
    result += list[i] - 10

print(result)
