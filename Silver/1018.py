import sys

N, M = map(int, sys.stdin.readline().split())
Board_list = [0]*N
Operator_list = []
result = 0

for i in range(0, len(Board_list)):
  column_list = [0]*M
  column = list(sys.stdin.readline().strip())
  for j in range(0, len(column)):
    if column[j] == 'B':
      data = 0
    else:
      data = 1
    column_list[j] = data
  Board_list[i] = column_list
  

for r in range(N-8):
  for c in range(M-8):
    
    for row in range(r, r+9):
      column_list = [0]*8
      for col in range(c, c+9):
        column_list[col] = Board_list[row, col]
    print(column_list)


print(Board_list)