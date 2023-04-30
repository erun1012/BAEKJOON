from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())

N_dict = {}
NM_dict = {}

for i in range(0, N):
  N_dict[stdin.readline().rstrip()] = i
for j in range(0, M):
  R = stdin.readline().rstrip()
  if R in N_dict:
    NM_dict[R] = R

print(len(NM_dict))
for k in sorted(NM_dict.keys()):
  print(k)