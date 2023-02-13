import sys

N = int(sys.stdin.readline())
Spot_list = []

for i in range(N):
  Spot_list.append(list(sys.stdin.readline().split()))

Spot_list.sort(key=lambda y: int(y[1]))
Spot_list.sort(key=lambda x: int(x[0]))

for j in range(0, len(Spot_list)):
  print(Spot_list[j][0], Spot_list[j][1])