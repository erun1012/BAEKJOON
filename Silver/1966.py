import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
  N, M = map(int, sys.stdin.readline().rstrip().split())
  N_list = [0]*N
  for j in range(0, N):
    if j == M:
      N_list[j] = ['y',0]
    else:
      N_list[j] = ['n',0]
  V_list = list(map(int, sys.stdin.readline().rstrip().split()))
  for k in range(0, len(V_list)):
    N_list[k][1] = V_list[k]
    
  count = 0
  while len(N_list) >= 1:
    count += 1
    for m in range(0, len(N_list)):
      for l in range(0, len(N_list)-1):
        if N_list[0][1] < N_list[l+1][1]:
          N_list.append(N_list.pop(0))
          break
    if N_list[0][0] == 'y':
      print(count)
      break
    N_list.pop(0)