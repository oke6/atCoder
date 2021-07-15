insert_price = 10000
product_price = 2362
change = insert_price -product_price

coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
  count = change // i
  change = change % i
  print(str(i) + '円が' + str(count))