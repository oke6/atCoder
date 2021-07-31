
def calc(expression):
  stack = []
  for i in expression.split(' '):
    print(stack)
    if i == '+':
      b = stack.pop()
      a = stack.pop()
      stack.append(a + b)

    elif i == '-':
      b = stack.pop()
      a = stack.pop()
      stack.append(a - b)

    elif i == '*':
      b = stack.pop()
      a = stack.pop()
      stack.append(a * b)

    elif i == '/':
      b = stack.pop()
      a = stack.pop()
      stack.append(a // b)
    
    else:
      stack.append(int(i))

  return stack[0]

print(calc('4 6 2 + * 3 1 - 5 * -'))