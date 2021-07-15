def convert_year(n):
  wareki = ''
  year = 0
  if n >= 2019:
    wareki = '令和'
    year = n - 2019 + 1
  elif n >= 1989:
    wareki = '平成'
    year = n - 1989 + 1
  elif n >= 1926:
    wareki = '昭和'
    year = n - 1926 + 1
  elif n >= 1912:
    wareki = '大正'
    year = n - 1912 + 1
  else:
    wareki = '明治'
    year = n - 1868 + 1

  return wareki + str(year) + '年'

print(convert_year(1995))