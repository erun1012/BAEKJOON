import sys

T = int(sys.stdin.readline())
Result_list = [0]*T

for i in range(1, T+1):
  k = int(sys.stdin.readline())
  n = int(sys.stdin.readline())
  P_list = list(range(1, n+1))
  L_list = [0]*n
  for g in range(0, k):
    for j in range(0, len(P_list)):
      sum = 0
      for h in range(0, j+1):
        sum += P_list[h]
      L_list[j] = sum
    P_list = list(L_list)
  Result_list[i-1] = sum
  

for y in range(0, T):
  print(Result_list[y])