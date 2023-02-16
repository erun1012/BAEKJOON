import sys
from collections import deque

N = int(sys.stdin.readline())

for i in range(N):
  S = sys.stdin.readline()
  l = ''
  N_deque = deque()
  for j in range(0, len(S)):
    if S[j] == '(':
      N_deque.insert(j,'(')
      N_deque.insert(j+1,')')
  for k in N_deque:
    l += k
  if S[:-1] == l:
    print('YES')
  else:
    print('NO')