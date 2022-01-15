#!/usr/bin/env python3
#s = input()
n = int(input()) 

dict = {}
for i in range(n):
  s = input()
  if not (s in dict):
    dict[s] = 1
    print(i+1)