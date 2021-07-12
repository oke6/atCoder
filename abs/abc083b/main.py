#!/usr/bin/env python3
n, a, b = map(int, input().split())
answer = 0
for i in range(n+1):
  amount = sum(int(x) for x in str(i))
  if a <= amount <= b:
    answer += i
print(answer)
