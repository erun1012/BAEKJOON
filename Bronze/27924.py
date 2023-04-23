import sys

T, S = map(int, sys.stdin.readline().rstrip().split())

if (11 < T) and (T <= 16) and S == 0:
  print(320)
else:
  print(280)