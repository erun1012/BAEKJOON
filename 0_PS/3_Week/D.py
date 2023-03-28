import sys
N_list = [[1] * 2 for i in range(30)]
for i in range(2, len(N_list)):
  for j in range(1, len(N_list[i-1])):
    N_list[i].insert(-1, (N_list[i-1][j-1] + N_list[i-1][j]))
N_list[0] = [1]
    
n, k = map(int, sys.stdin.readline().rstrip().split())
print(N_list[n-1][k-1])