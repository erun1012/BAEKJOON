import sys

def fac(n):
  data = 1
  for i in range(1, n+1):
    data *= i
  return data

N = int(sys.stdin.readline())
if N == 0:
  N = 1
result = fac(N)

count = 0
for i in range(len(str(result))-1, -1, -1):
  if str(result)[i] == '0':
    count += 1
  else:
    break
print(count)