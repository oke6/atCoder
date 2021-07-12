#!/usr/bin/env python3
n = int(input())  # nは入力回数
num_list = [list(map(int, input().split())) for _ in range(n)]

status=0
t=0
x=0
y=0
for i,v in enumerate(num_list):
  time=v[0]-t
  move=abs(v[1]+v[2]-x-y)
  if time < move:
    status=1
    break
  else:
    if time%2 != move%2:
      status=1
      break
  t=v[0]
  x=v[1]
  y=v[2]

if status == 0:
  print("Yes")
else:
  print("No")

      

