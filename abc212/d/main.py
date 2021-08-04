#!/usr/bin/env python3
from heapq import heappop, heappush

n = int(input()) 

result = []
bag = []
tmp = 0
priority_queue = []
for _ in range(n):
  inputs = list(map(int, input().split()))
  if inputs[0] == 1:
    heappush(priority_queue, inputs[1] - tmp) 
  elif inputs[0] == 2:
    tmp += inputs[1]
  else:
    result.append(heappop(priority_queue) + tmp)

for i in result:
  print(i)
