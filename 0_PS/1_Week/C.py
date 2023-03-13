import sys
from collections import Counter

N_list = list(sys.stdin.readline().rstrip().split())
A = int(Counter(N_list).most_common()[0][0])

Max = int(max(N_list))

if N_list[0] == N_list[1] and N_list[1] == N_list[2]:
  print(10000+Max*1000)
elif N_list[0] != N_list[1] and N_list[1] != N_list[2] and N_list[2] != N_list[0]:
  print(Max*100)
else:
  print(1000+A*100)