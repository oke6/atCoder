data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

changed = True
for i in range(len(data)):

  if not changed:
    break

  changed = False
  for j in range(len(data) - i - 1):
    if (data[j] > data[j+1]):
      data[j], data[j+1] = data[j+1], data[j]
      changed = True


print(data)