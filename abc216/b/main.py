#!/usr/bin/env python3
n = int(input()) 

S = []
T = []

names = {}
for i in range(n):
  s, t = input().split()
  if s in names:
    if t in names[s]:
      print('Yes')
      exit()
  
  names[s] = {t: 1}

print('No')