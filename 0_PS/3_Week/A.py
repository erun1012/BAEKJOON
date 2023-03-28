import sys

N = int(sys.stdin.readline())

result = 0
if (((N+1) // 2)-1) + ((N+1) // 2) == N:
  result += 1
for i in range(1, (N+1)//2):
  if N % i == 0:
    if (N // i) - ((i-1)/2) <= 0:
      continue
    else:
      print(i, (N // i) - (i-1)/2)
      result += 1
print(result)