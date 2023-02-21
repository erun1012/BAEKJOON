import sys
from collections import deque

while True:
  N = str(sys.stdin.readline().rstrip())

  if N == '.':
    break

  else:
    result = ''
    N_deque = deque()
    for j in range(0, len(N)):
      i = N[j]
      if i == '(':
        N_deque.insert(j,'(')
        N_deque.insert(j+1,')')
      elif i == '[':
        N_deque.insert(j,'[')
        N_deque.insert(j+1,']')
      elif i != ']' and i != ')':
        N_deque.insert(j, i)

    for k in N_deque:
      result += k

    if N == result and result[-1] == ".":
      print('yes')
    else:
      print('no')