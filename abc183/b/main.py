#!/usr/bin/env python3
sx, sy, gx, gy = map(int, input().split())

dx = (sy+gy)/(sx-gx)
x=(0-(sy-dx*sx))/dx
print(x)
