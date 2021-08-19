#!/usr/bin/env python3
h, w = map(int, input().split())

A = []
B = []
for i in range(h):
  A.append(list(map(int, input().split())))

for i in range(h):
  B.append(list(map(int, input().split())))

diff = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
  for j in range(w):
    diff[i][j] = A[i][j] - B[i][j]

ans = 0
for i in range(h-1):
  for j in range(w-1):
    tmpDiff = diff[i][j]
    diff[i][j] -= tmpDiff
    diff[i+1][j] -= tmpDiff
    diff[i][j+1] -= tmpDiff
    diff[i+1][j+1] -= tmpDiff
    ans += abs(tmpDiff)

flag = True

for i in range(h):
  if diff[i][w-1] != 0:
    flag = False
    break

for i in diff[h-1]:
  if i != 0:
    flag = False
    break

if flag:
  print('Yes')
  print(ans)
else:
  print('No')