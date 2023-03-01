import sys

def Cut(li, n):
  count = 0
  for j in range(0, len(li)):
    count += (li[j] // n)
  return count

N, K = map(int, sys.stdin.readline().rstrip().split())
N_list = [0] * N

for i in range(N):
  N_list[i] = int(sys.stdin.readline().rstrip())

N_list.sort()

start = 0
end = (2**31)-1
max = 0
if N == 1 and K == 1:
  print(N_list[0])
else:
  while start <= end:
    mid = (start + end) // 2
    value = Cut(N_list, mid)
    if value >= K:
      max = mid
      start = mid + 1
    elif value < K:
      end = mid - 1
  
  print(max)