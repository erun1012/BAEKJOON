import sys

N = int(sys.stdin.readline().rstrip())
N_list = [0]*201

S_list = list(map(int, sys.stdin.readline().rstrip().split()))

for i in S_list:
  N_list[i+100] += 1

v = int(sys.stdin.readline().rstrip())
print(N_list[v+100])