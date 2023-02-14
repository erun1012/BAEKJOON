import sys
from copy import deepcopy

N, M = map(int, sys.stdin.readline().split())
Board_list = [0]*N
Operator_list = [0]*8
result_list = []

for i in range(0, len(Board_list)):  # N*M 보드를 Board_list에 저장, B는 0으로, W는 1로 저장합니다
  column_list = [0]*M
  column = list(sys.stdin.readline().strip())
  for j in range(0, len(column)):
    if column[j] == 'B':
      data = 0
    else:
      data = 1
    column_list[j] = data
  Board_list[i] = column_list
  

for r in range(N-7):  # 8*8로 만들 수 있는 모든 경우의수를 진행합니다
  for c in range(M-7):
    row_count = -1
    for row in range(r, r+8):  # 8*8 보드를 만듭니다
      row_count += 1
      column_list = [0]*8
      col_count = -1
      for col in range(c, c+8):
        col_count += 1
        column_list[col_count] = Board_list[row][col]
      Operator_list[row_count] = column_list

    OP_list = [Operator_list, deepcopy(Operator_list)]  # 8*8보드를 OP_list에 저장합니다. 2개를 저장하는 이유는 가장 왼쪽 위 (0,0)이 바뀌는 경우도 계산하기 위해서입니다.
    if OP_list[1][0][0] == 0:
      OP_list[1][0][0] = 1
    else:
      OP_list[1][0][0] = 0
    
    for asdf in range(2):
      result = 0
      go = OP_list[asdf]
      result += asdf
      
      for R in range(0, 8):  # 8*8 보드에서 체스판을 다시 칠하는 경우를 계산합니다
        for C in range(0, 7):
          if (R != 0 and C == 0):
            if go[R-1][C] + go[R][C] == 0:
              result += 1
              if go[R][C] == 1:
                go[R][C] = 0
              else:
                go[R][C] = 1
          if go[R][C] + go[R][C+1] == 1:
            continue
          else:
            result += 1                                           
            if go[R][C+1] == 1:
              go[R][C+1] = 0
            else:
              go[R][C+1] = 1
      result_list.append(result)  # 칠하는 횟수를 result에 저장합니다

result_list.sort()
print(result_list[0])  # 최소값 출력