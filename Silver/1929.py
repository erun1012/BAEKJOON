import sys

M, N = map(int, sys.stdin.readline().rstrip().split())

for i in range(M, N+1):
  count = 1
  if i != 1:
    for j in range(2, int(i**0.5)+1):  # 특정 수의 제곱근을 구해, 그 제곱근까지의 약수를 구하면 해당 약수를 포함하는 수를 모두 제거할 수 있다
      if i % j == 0:
        count = 0
        break
    if count == 1:
      print(i)