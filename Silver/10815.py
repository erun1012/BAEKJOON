import sys

N = int(sys.stdin.readline().rstrip())

Q_list = list(map(int,sys.stdin.readline().rstrip().split()))

Q_list.sort()

M = int(sys.stdin.readline().rstrip())

F_list = list(map(int,sys.stdin.readline().rstrip().split()))

Result_list = [0]*(len(F_list))

for i in range(0, len(F_list)):
  start = 0
  end = len(Q_list) - 1
  while True:
    mid = (start + end) // 2
    if F_list[i] == Q_list[mid]:
      Result_list[i] = 1
      break
    elif F_list[i] > Q_list[mid]:
      start = mid + 1
    elif F_list[i] < Q_list[mid]:
      end = mid - 1
    if start > end:
      Result_list[i] = 0
      break

for j in Result_list:
  print(j,end=" ")