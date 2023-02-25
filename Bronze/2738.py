import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
pro_list = [[0] * M for i in range(N)]

for i in range(2):
  for j in range(N):
    m_list = list(map(int, sys.stdin.readline().rstrip().split()))
    for k in range(0, len(m_list)):
      pro_list[j][k] += m_list[k]

for l in range(0, len(pro_list)):
  for m in range(0, len(pro_list[l])):
    print(pro_list[l][m], end=' ')
  print()