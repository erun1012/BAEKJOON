import sys
from collections import deque

N = int(sys.stdin.readline())
N_deque = deque()

for i in range(1, N+1):
  N_deque.append(i)

while len(N_deque) > 1:
  N_deque.popleft()
  N_deque.append(N_deque.popleft())

print(N_deque.pop())