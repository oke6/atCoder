#!/usr/bin/env python3
n = int(input()) 
list = list(map(int, input().split()))

list.sort()
result = 1

for i in range(n):
  result = result * max(0,(list[i] - i)) % 1000000007
  if result == 0:
    break

print(result) 
