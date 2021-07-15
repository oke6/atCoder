def get_uru(start, end):
  uru = []
  for i in range(start, end + 1):
    if (i % 4 == 0) and not (i % 100 == 0 and i % 400 != 0):
      uru.append(i)
  return uru

print(get_uru(1990, 2110))