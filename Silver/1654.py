import sys

def Cut(li, n, ma):
  count = 0
  for j in range(0, len(li)):
    count += (li[j] // n)
    if count > ma:
      break
  return count

N, K = map(int, sys.stdin.readline().rstrip().split())
N_list = [0] * N

for i in range(N):
  N_list[i] = int(sys.stdin.readline().rstrip())

N_list.sort()

start = 0
end = (2**31)-1
repe = 0
while True:
  if N == 1 and K == 1:
    print(N)
    break
  mid = (start + end) // 2
  if mid == repe:
    print(mid)
    break
  value = Cut(N_list, mid, K)
  if value == K:
    for k in range(mid, end):
      value = Cut(N_list, k, K)
      if value < K:
        print(k - 1)
        break
    break
  elif value > K:
    start = mid + 1
    repe = mid
  elif value < K:
    end = mid -1
    repe = mid

