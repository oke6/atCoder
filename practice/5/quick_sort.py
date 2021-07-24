data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

def quick_sort(data):
  if len(data) <= 1:
    return data

  pivot = data[0]
  
  left = quick_sort([i for i in data[1:] if i <= pivot])
  right = quick_sort([i for i in data[1:] if i > pivot])

  return left + [pivot] + right
    
print(quick_sort(data))