import sys

M = int(sys.stdin.readline())

S = [0] * 20

for i in range(M):
  do = list(map(str, sys.stdin.readline().rstrip().split()))
  if do[0] == "add":
    S[int(do[1]) - 1] = 1
  elif do[0] == "remove":
    S[int(do[1]) - 1] = 0
  elif do[0] == "check":
    if S[int(do[1]) - 1] == 1:
      print(1)
    else:
      print(0)
  elif do[0] == "toggle":
    if S[int(do[1]) - 1] == 1:
      S[int(do[1]) - 1] = 0
    else:
      S[int(do[1]) - 1] = 1
  elif do[0] == "all":
    for j in range(0, 20):
      S[j] = 1
  elif do[0] == "empty":
    for j in range(0, 20):
      S[j] = 0