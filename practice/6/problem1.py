def convert(binary):
  numList = list(binary)
  result = []
  count = 0
  current = '0'
  
  for i in range(len(numList)):
    if (numList[i] == current):
      count += 1
    else:
      result.append(count)
      current = numList[i]
      count = 1
    
  result.append(count)

  return result

print(convert('000000111111100111000000001111'))