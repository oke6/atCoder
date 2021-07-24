import os

#深さ優先探索
def search(dir, name):
  for element in os.listdir(dir):
    if element == name:
      print(dir + element)
    if os.path.isdir(dir + element):
      if os.access(dir + element, os.R_OK):
        search(dir + element + '/', name)

search('/', 'book')