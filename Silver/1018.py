import sys

N, M = map(int, sys.stdin.readline().split())
Board_list = [0]*N
Operator_list = [0]*8
result = 0
result_list = []

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
  

for r in range(N-7):
  for c in range(M-7):
    row_count = -1
    for row in range(r, r+8):
      row_count += 1
      column_list = [0]*8
      col_count = -1
      for col in range(c, c+8):
        col_count += 1
        column_list[col_count] = Board_list[row][col]
      Operator_list[row_count] = column_list
    print(Operator_list)
    
    result = 0
    for R in range(0, 8):
      for C in range(0, 7):
        if (R != 0 and C == 0):
          if Operator_list[R-1][C] + Operator_list[R][C] == 0:
            result += 1
            if Operator_list[R][C] == 1:
              Operator_list[R][C] = 0
            else:
              Operator_list[R][C] = 1
        if Operator_list[R][C] + Operator_list[R][C+1] == 1:
          continue
        else:
          result += 1
          if Operator_list[R][C+1] == 1:
            Operator_list[R][C+1] = 0
          else:
            Operator_list[R][C+1] = 1
    result_list.append(result)
    print(result_list[-1])


print(Board_list)
print(Operator_list)
result_list.sort()
print(result_list)
print(result_list[0], len(result_list))