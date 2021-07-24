data = [9,4,5,2,8,3,7,8,3,2,6,5,7,9,2,9]

dict = {}
for i in data:
  if i in dict:
    dict[i] += 1
  else:
    dict[i] = 1
  
result = []
for j in range(1, 10):
  if j in dict:
    result = result + [j] * dict[j]
print(result)