#!/usr/bin/env python3
n = int(input()) 
list = list(map(int, input().split()))

count = 0
while all(a%2==0 for a in list):
  list=[a/2 for a in list]
  count += 1

print(count)


