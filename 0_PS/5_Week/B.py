import sys

S = sys.stdin.readline().rstrip()
A = ""
for i in range(len(S)-1, -1, -1):
  A += S[i]
if S == A:
  print(1)
else:
  print(0)