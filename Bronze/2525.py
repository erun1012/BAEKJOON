import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
C = int(sys.stdin.readline().rstrip())

B += C
if B >= 60:
  A = B // 60 + A
  B = B % 60

if A >= 24:
  A -= 24
print(A, B)