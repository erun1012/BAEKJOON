from sys import stdin

N = int(stdin.readline().rstrip())

N_list = list(map(int, stdin.readline().rstrip().split()))

N_list.sort()

sum = 0
result = 0
for i in range(0, len(N_list)):
  sum += N_list[i]
  result += sum
print(result)