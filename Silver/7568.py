import sys
from copy import deepcopy

N = int(sys.stdin.readline().rstrip())
N_list = []
Result = [0]*N

for i in range(N):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  N_list.append([x, y])
X_list = deepcopy(N_list)
Y_list = deepcopy(N_list)
X_list.sort(key=lambda x: x[0])
Y_list.sort(key=lambda y: y[1])
print(N_list,"\n", X_list,"\n", Y_list)