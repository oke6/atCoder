memo = {1: 1, 2: 1}

def fibonacci(n):
  if n in memo:
    return memo[n]
  memo[n] = fibonacci(n-1) + fibonacci(n-2)
  return memo[n]

def fibonacci2(n):
  fib = [1,2]
  for i in range(2, n):
    fib.append(fib[i-2] + fib[i-1])
  return fib[n-1]

print(fibonacci(10))