import sys

N, M, B = map(int, sys.stdin.readline().rstrip().split())
N_list = [0] * N

for j in range(0, len(N_list)):
  N_list[j] = list(map(int, sys.stdin.readline().rstrip().split()))

measure = 0
high, time1, time2 = 0, 0, 0
for k in range(0, len(N_list)):
  for l in range(0, len(N_list[k])):
    if N_list[k][l] >= N_list[0]