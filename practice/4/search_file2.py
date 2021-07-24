import os

#幅優先探索
queue = ['/']

while len(queue) > 0:
  dir = queue.pop()
  for element in os.listdir(dir):
    if element == 'book':
      print(dir + element)
    if os.path.isdir(dir + element):
      if os.access(dir + element, os.R_OK):
        queue.append(dir + element + '/')