import sys

while True:
  N = int(sys.stdin.readline())
  if N == 0:
    break
  start, end = 1, 50
  while start <= end:
    mid = (start + end) // 2
    if mid == N:
      print(mid, end="\n")
      break
    elif mid < N:
      print(mid, end=' ')
      start = mid + 1
    elif mid > N:
      print(mid, end=' ')
      end = mid - 1