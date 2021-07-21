#!/usr/bin/env python3
n, k = map(int, input().split())
list = list(map(int, input().split()))

tempList = list[0:k]
count = len(set(tempList))
result = count

colors = {}
for color in tempList:
  if color in colors:
    colors[color] += 1
  else:
    colors[color] = 1


for j in range(n-k):
  tmpDel = list[j]
  tmpAdd = list[j+k]

  if (colors[tmpDel] == 1):
    del colors[tmpDel]
    count -= 1
  else:
    colors[tmpDel] -= 1

  if tmpAdd in colors:
    colors[tmpAdd] += 1
  else:
    colors[tmpAdd] = 1
    count += 1

  result = max(result, count)

print(result)