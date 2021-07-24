data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(1, len(data)):
  j = i - 1
  temp = data[i]
  while (j >= 0) & (data[j] > temp):
    data[j+1] = data[j]
    j -= 1
  data[j+1] = temp

print(data)