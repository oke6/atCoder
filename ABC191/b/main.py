#!/usr/bin/env python3
N, X = map(int, input().split())
list = list(map(int, input().split()))

mylist = [item for item in list if item!=X] 

L=[str(a) for a in mylist]
L=" ".join(L)
print(L)