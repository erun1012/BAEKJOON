import sys
from collections import deque

N = int(sys.stdin.readline())
N_deque = deque(range(0, N))

for i in range(0, len(N_deque)):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  N_deque[i] = [x, y]