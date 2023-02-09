import sys
c = int(sys.stdin.readline())
N_list = [0] * 10001

for i in range(c):
  N = int(sys.stdin.readline())
  N_list[N] += 1

for j in range(0, len(N_list)):
  if N_list[j] == 0:
    continue
  else:
    for k in range(0, N_list[j]):
      print(j)