from sys import stdin

N,K = map(int, stdin.readline().rstrip().split())

N_list = [0]*N

for i in range(0, N):
  R = int(stdin.readline())
  N_list[i] = R
  
count = 0
while K > 0:
  for j in range(len(N_list)-1, -1, -1):
    if K // N_list[j] != 0:
      count += K // N_list[j]
      K = K % N_list[j]
    N_list
print(count)