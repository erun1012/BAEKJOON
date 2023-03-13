import sys
import math

N_list = [0]*9

N = str(sys.stdin.readline().rstrip())

for i in N:
  if i == "6" or i == "9":
    N_list[6] += 1
  else:
    N_list[int(i)] += 1

MAX = 0
for j in range(0, len(N_list)):
  if j == 6:
    if int((N_list[j]+1)/2) > MAX:
      MAX = int((N_list[j]+1)/2)
  else:
    if MAX < N_list[j] :
      MAX = N_list[j] 

print(MAX)