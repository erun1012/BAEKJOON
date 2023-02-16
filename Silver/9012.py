import sys
from collections import deque

N = int(sys.stdin.readline())

for i in range(N):
  S = sys.stdin.readline().rstrip()
  result = ''
  N_deque = deque()
  for j in range(0, len(S)):
    if S[j] == '(':
      N_deque.insert(j,'(')
      N_deque.insert(j+1,')')

  for k in N_deque:
    result += k

  if S == result:
    print('YES')
  else:
    print('NO')