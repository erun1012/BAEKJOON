import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
N_deque = deque(range(0,N))

for i in range(N):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  N_deque[i] = [x, y]

for j in N_deque:
  ranking = 1
  for k in N_deque:
    if j[0] < k[0] and j[1] < k[1]:
      ranking += 1
  print(ranking, end= " ")