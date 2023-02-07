def make_result(s):
  global k
  for i in range(s, int(N)):
    sum, result = 0, 0
    for x in str(i):
      sum += int(x)
    result = int(sum) + i
    if result == int(N):
      print(i)
      k = 1
      break

N = input()
length = len(N)
d, k = 0, 0

if length >= 3:
  d = (10 * (length - 1)) * (int(N[0]) - 1)

make_result(d)

if k == 0:
  print(0)