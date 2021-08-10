#!/usr/bin/env python3
import itertools

N = int(input()) 
A = []
for i in range(N):
  array = list(map(int, input().split()))
  A.append(array)

M = int(input())

rumors = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):
  x, y = map(int, input().split())
  rumors[x-1][y-1] = 1
  rumors[y-1][x-1] = 1

permList = list(itertools.permutations(range(N)))

ans = int(1e9)
flag = False
for perm in permList:
  tmp = 0
  for j in range(N):
    if j < N-1 and rumors[perm[j]][perm[j+1]] == 1:
      break
    tmp += A[perm[j]][j]
  else:
    ans = min(ans, tmp)
    flag = True

if flag:
  print(ans)
else:
  print(-1)