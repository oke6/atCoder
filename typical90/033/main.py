#!/usr/bin/env python3
H, W = map(int, input().split())

if (H == 1) or (W == 1):
  print(H*W)
  exit()

print(((H+1)//2)*((W+1)//2))
