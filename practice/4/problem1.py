N = 10
count = 0

def search(pos, steps):
  global count

  if pos == N:
    print(steps)
    count = count + 1
  else:
    for i in range(pos+1, N+1):
      steps.append(i)
      search(i, steps)
      steps.pop()
      
search(1, [1])
print(count)