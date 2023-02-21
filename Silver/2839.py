import sys

N = int(sys.stdin.readline().rstrip())
if N%5 == 0:
  print(int(N/5))
else:
  count = 0
  while N > 0:
    N -= 3
    count += 1
    if N%5 == 0:
      print(int(N/5+count))
      break
    elif N == 1 or N == 2:
      print(-1)
      break
    elif N == 0:
      print(count)
      break