import sys

N = int(sys.stdin.readline())
A = int(sys.stdin.readline())

if N >= 6:
  print("Love is open door")
else:
  for i in range(N-1):
    if A == 0:
      A = 1
    elif A == 1:
      A = 0
    print(A)