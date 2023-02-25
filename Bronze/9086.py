import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
  S = str(sys.stdin.readline().rstrip())
  print(S[0]+S[-1])