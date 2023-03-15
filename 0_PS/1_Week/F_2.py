from sys import stdin
from collections import Counter

N_list = [0]*6

S = str(stdin.readline().rstrip())
I_list = list(map(int, stdin.readline().rstrip().split()))
for i in range(0, len(I_list)):
  N_list[I_list[i] - 1] += 1
  
Check_list = []
for j in range(0, len(N_list)):
  if N_list[j] != 0:
    Check_list.append([j+1, N_list[j]])

print(N_list, I_list, Check_list)