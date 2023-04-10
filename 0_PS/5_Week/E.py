import sys

T = int(sys.stdin.readline().rstrip())

for i in T:
  N, M = map(int, sys.stdin.readline().rstrip().split())
  for i in M:
    a, b = map(int, sys.stdin.readline().rstrip().split())