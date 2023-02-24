import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
length_deque = deque()

for i in range(N):
  length_deque.append(int(sys.stdin.readline().rstrip()))

max = sum(length_deque) // 11

j = 0
while True:
  count_deque = deque()
  j += 1000
  for k in length_deque:
    count_deque.append(int(k//j))
  if sum(count_deque) <= K:
    print(j, count_deque)
    break

for l in range(100):
  j += 1
  count = 0
  for k in length_deque:
    count += (k//j)
  if count > K:
    result