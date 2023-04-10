import sys
import math

def prime(num):
    if num == 1:
      return 0
    for j in range(2, int(math.sqrt(num) + 1)):
      if num % j == 0:
        return 0
    return 1

while True:
  n = int(sys.stdin.readline().rstrip())
  if n == 0:
    break
  count = 0
  for i in range(n+1, (n*2)+1):
    if prime(i):
      count += 1
  print(count)