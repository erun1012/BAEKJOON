import sys
from collections import deque

N = int(sys.stdin.readline())
N_deque = deque(range(0, N))
P_deque = deque(range(1, N+1))
Stack_deque = deque(range(0,1))
Result_deque = deque()

for i in range(0, N):
  n = int(sys.stdin.readline())
  N_deque[i] = n

b = 0
for j in range(0, len(N_deque)):
  while Stack_deque[-1] != N_deque[j]:
    if (N_deque[j] != Stack_deque[-1]):
      if (N_deque[j] < Stack_deque[-1]):
        Result_deque = ["NO"]
        b = 1
        break
    Stack_deque.append(P_deque.popleft())
    Result_deque.append("+")
  if b == 1:
    break
  Stack_deque.pop()
  Result_deque.append("-")

for k in Result_deque:
  print(k)