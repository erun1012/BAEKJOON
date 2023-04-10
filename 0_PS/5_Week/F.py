import sys

N = int(sys.stdin.readline())

B_list = []

G = int(sys.stdin.readline())


for i in range(G):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  if i == 0:
    B_list.append([a, b])
    continue
  num = 0
  for j in range(0, len(B_list)):
    A = a in B_list[j]
    B = b in B_list[j]
    if A + B == 0:
      continue
    else:
      if A == 0:
        B_list[j].append(a)
      elif B == 0:
        B_list[j].append(b)
      num = 1
  if num == 0:
    B_list.append([a, b])
    
for k in range(0, len(B_list)):
  if 1 in B_list[k]:
    print(len(B_list[k]) - 1)
    break