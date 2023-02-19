# 정답 코드 1
import sys

N = int(sys.stdin.readline())
N_list = list(range(0, N))

for i in range(N):
  x, y = map(int, sys.stdin.readline().split())
  N_list[i] = [x, y]

N_list.sort(key=lambda y: (y[1], y[0]))

for n in N_list:
  print(n[0], n[1])



# 정답 코드 2
import sys

N = int(sys.stdin.readline())
N_list = list(range(0, N))

for i in range(N):
  x, y = map(int, sys.stdin.readline().split())
  N_list[i] = [x, y]

N_list.sort(key=lambda y: y[1])

j = 0
while (j < (len(N_list)-1)):
  N_sort_list = []
  count = 1
  if N_list[j][1] == N_list[j+1][1]:
    k = j
    while N_list[k][1] == N_list[k + 1][1]:
      N_sort_list.append(N_list[k])
      k += 1
      count += 1
      if (k+1) >= len(N_list):
        break
    N_sort_list.append(N_list[k])
    N_sort_list.sort(key=lambda x: x[0])
    for l in range(0, len(N_sort_list)):
      N_list[l + j] = N_sort_list[l]
  j += count

for n in N_list:
  print(n[0], n[1])