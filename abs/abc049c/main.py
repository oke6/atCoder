#!/usr/bin/env python3
import re
S = input()
print("YES" if re.match("^(dreamer|dream|erase|eraser)+$", S) else "NO")
