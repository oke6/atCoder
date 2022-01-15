#!/usr/bin/env python3
import itertools

N = int(input())
A =[]
for i in range(N):
  A.append(list(map(int, input().split())))

rumor = [[0 for _ in range(N)] for _ in range(N)]
M = int(input())
for i in range(M):
  x, y = map(int, input().split())
  rumor[x-1][y-1] = 1
  rumor[y-1][x-1] = 1

nums = []
for i in range(1, N+1):
  nums.append(i)
permutations = itertools.permutations(nums)


ans = 10000
flag = False
for permutation in permutations:
  time = 0
  prev = 0
  canFinish = True
  for i in range(N):
    current = permutation[i]
    if (prev != 0):
      if (rumor[prev-1][current-1] == 1):
        canFinish = False
        continue
    time += A[current-1][i]
    prev = current
  
  if (canFinish):
    ans = min(ans, time)
    flag = True

if (flag):
  print(ans)
else:
  print(-1)