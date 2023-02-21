import sys
from collections import deque

K = int(sys.stdin.readline().rstrip())
K_deque = deque()

for i in range(K):
  N = int(sys.stdin.readline().rstrip())
  if N == 0:
    K_deque.pop()
  else:
    K_deque.append(N)
    
print(sum(K_deque))