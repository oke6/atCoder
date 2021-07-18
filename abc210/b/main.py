#!/usr/bin/env python3
n = int(input()) 
s = input()

for i in range(n+1):
  if s[i] == '1':
    if i % 2 == 0:
      print('Takahashi')
    else:
      print('Aoki')
    break