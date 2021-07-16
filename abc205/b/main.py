#!/usr/bin/env python3
n = int(input()) 
list = list(map(int, input().split()))

if len(list) != len(set(list)):
  print('No')
  exit()

if sum(list) != n*(n+1)/2:
  print('No')
  exit()

print('Yes')