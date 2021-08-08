#!/usr/bin/env python3
n, k = map(int, input().split())

def toBase9(num):
  if num == 0:
    return '0'

  numBase9 = ''
  while(num > 0):
    numBase9 = str((num % 9)) + numBase9
    num = num // 9
  return numBase9

numBase10 = int(str(n), 8)

for i in range(k):
  numBase9 = toBase9(numBase10)
  numBase8 = numBase9.replace('8', '5')
  numBase10 = int(numBase8, 8)

print(numBase8)
  


