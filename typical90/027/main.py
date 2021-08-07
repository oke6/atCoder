#!/usr/bin/env python3
n = int(input()) 

dict = {}
for i in range(n):
  name = input()
  if not (name in dict.keys()):
    print(i+1)
    dict[name] = 1



