import sys

N = int(sys.stdin.readline())
P_list = []

for i in range(N):
  P_list.append(list(sys.stdin.readline().split()))

P_list.sort(key=lambda x: int(x[0]))

for j in range(0, len(P_list)):
  print(P_list[j][0], P_list[j][1])