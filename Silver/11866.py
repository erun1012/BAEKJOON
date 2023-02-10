import sys

N, K = map(int, sys.stdin.readline().split())

N_list = list(range(1, N+1))
POP_list, result = [], []
count = -1

for i in range(0, N):
  count += K
  while count >= len(N_list):
    count -= len(N_list)
    for j in range(0, len(POP_list)):
      N_list.remove(POP_list[j])
    POP_list.clear()
  a = N_list[count]
  POP_list.append(a)
  result.append(a)

print("<",end="")
for j in range(0, len(result)):
  if j != len(result) - 1:
    print(str(result[j])+", ",end="")
  else:
    print(str(result[j])+">") 