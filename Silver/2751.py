import sys

N = int(sys.stdin.readline())

N_list = [0]*2000002

for i in range(N):
  num = int(sys.stdin.readline())
  N_list[num+1000000] = 1

for j in range(0, len(N_list)):
  if N_list[j] == 1:
    print(j-1000000)