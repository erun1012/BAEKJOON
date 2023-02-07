N, M = map(int, input().split())
Card_list = list(map(int, input().split()))

Card_list.sort()
result = 0

for i in range(0, N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      if Card_list[i] + Card_list[j] + Card_list[k] > M:
        continue
      else:
        result = max(result, Card_list[i] + Card_list[j] + Card_list[k])

print(result)