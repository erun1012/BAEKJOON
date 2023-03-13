import sys
N_list = [0]*10

mat = 1
for i in range(3):
  mat *= int(sys.stdin.readline().rstrip())

for j in str(mat):
  N_list[int(j)] += 1

for k in range(0, len(N_list)):
  print(N_list[k])