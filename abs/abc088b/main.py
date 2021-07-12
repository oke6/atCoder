#!/usr/bin/env python3
a = input()
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)

alice=0
bob=0
for i, v in enumerate(num_list):
  if i%2==0:
    alice += v
  else:
    bob += v

print(alice - bob)
