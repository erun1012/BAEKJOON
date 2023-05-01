from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
N_dict = {}

for i in range(N):
  loc, pas = map(str, stdin.readline().rstrip().split())
  N_dict[loc] = pas

for j in range(M):
  f = stdin.readline().rstrip()
  print(N_dict[f])