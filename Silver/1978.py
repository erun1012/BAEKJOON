import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
count = 0

# 소수 판별 함수
def is_prime_number(x):
  if x == 1:
    return 0
  for i in range(2, x):
      if x % i == 0:
          return 0
  return 1

for j in N_list:
  count += is_prime_number(j)

print(count)