import sys
import math
A, B, V = map(int,sys.stdin.readline().split())
t = 0

if (V-A) >=0:
  t = math.ceil( (V-A) / (A-B))

print(t + 1)