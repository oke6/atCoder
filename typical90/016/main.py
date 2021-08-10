#!/usr/bin/env python3
n = int(input())

a, b, c = map(int,input().split())

num = 9999
for i in range(num):
    for j in range(num - i):
        k, r = divmod(n - a*i - b*j, c)
        if r == 0 and k >= 0:
            num = min(num, i+j+k)

print(num)