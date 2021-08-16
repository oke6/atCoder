#!/usr/bin/env python3
import copy

n = int(input()) 
S = list(map(int, input().split()))
T = list(map(int, input().split()))

ans = copy.copy(T)

for i in range(n):
  prev = i-1
  if i == 0:
    prev = n-1

  ans[i] = min(T[i], ans[prev] + S[prev])

for i in range(n):
  prev = i-1
  if i == 0:
    prev = n-1

  ans[i] = min(T[i], ans[prev] + S[prev])

for i in range(n):
  print(ans[i])