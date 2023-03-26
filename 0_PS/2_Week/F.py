N_list = [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97]
for i in range(1, 10001):
  result = 1
  if i in N_list:
    print(i)
    continue
  elif i >= 100:
    for k in range(i-37, i, 1):
      count = 0
      for j in str(k):
        count += int(j)
      if k + count == i:
        result = 0
        break
    if result == 1:
      print(i)