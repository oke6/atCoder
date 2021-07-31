text = list('SHOEISHA SESHOP')
pattern = list('SHA')

skip = {}
for i in range(len(pattern) - 1):
  skip[pattern[i]] = len(pattern) - i - 1

i = len(pattern) - 1
while i < len(text):
  match = True
  for j in range(len(pattern)):
    if text[i - j] != pattern[len(pattern) - j - 1]:
      match = False
      break

  if not match:
    if text[i] in skip:
      i += skip[text[i]]
    else:
      i += len(pattern)
  else:
    print(i - len(pattern) + 1)
    break
    
