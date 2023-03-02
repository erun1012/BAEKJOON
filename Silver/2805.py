import sys

def Sum(LIST, Leng):
  sum = 0
  for i in range(0, len(LIST)):
    if LIST[i] > Leng:
      sum += (LIST[i] - Leng)
  return sum

N, M = map(int, sys.stdin.readline().rstrip().split())

N_list = list(sorted(map(int, sys.stdin.readline().rstrip().split())))

start, end = 0, N_list[-1]
max = 0

if N == 1:
  print(N_list[0] - M)
else:
  while start <= end:
    mid = (start + end) // 2
    value = Sum(N_list, mid)
    if value >= M:
      max = mid
      start = mid + 1
    elif value < M:
      end = mid - 1
  print(max)