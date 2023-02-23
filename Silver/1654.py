import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
length_deque = deque()

for i in range(N):
  length_deque.append(int(sys.stdin.readline().rstrip()))

max = sum(length_deque) // 11

for j in range(max, 0 , -1):
  error = 0
  count = 0
  for k in range(0, len(length_deque)):
    count += int(length_deque[k]/j)
  if count == K:
    print(j)
    break