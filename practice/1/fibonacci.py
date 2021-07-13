def fibonacci(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1
  else:
    return fibonacci(n-2) + fibonacci(n-1)

for i in range(8):
  print(fibonacci(i))