#!/usr/bin/env python3
a,b,c = map(int, input().split())

list = [a,b,c]
list.sort()
print(list[2] + list[1])
