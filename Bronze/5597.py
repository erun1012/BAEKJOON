import sys
S_list = [0]*31

for i in range(28):
  S = int(sys.stdin.readline().rstrip())
  S_list[S] = 1

for j in range(1, len(S_list)):
  if S_list[j] == 0:
    print(j)