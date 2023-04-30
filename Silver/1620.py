from sys import stdin

N, M = map(int, stdin.readline().split())

Pok_dict = {}

for i in range(0, N):
  R = str(stdin.readline().rstrip())
  Pok_dict[R] = i + 1
  Pok_dict['{0}'.format(i + 1)] = R
for j in range(0, M):
  print(Pok_dict.get(str(stdin.readline().rstrip())))