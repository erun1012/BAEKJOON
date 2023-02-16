from collections import deque, Counter
import sys

N = int(sys.stdin.readline().rstrip())

N_list = sorted(map(str, sys.stdin.readline().rstrip().split()))
N_deque = deque(N_list)
S = int(sys.stdin.readline().rstrip())
S_deque = deque(map(str, sys.stdin.readline().rstrip().split()))

result = deque()
count = Counter(N_deque)

for k in S_deque:
  if k in count:
    result.append(count[k])
  else:
    result.append(0)
    
for l in result:
  print(l, end=' ')