# https://hongcoding.tistory.com/50
from sys import stdin

N, K = map(int, stdin.readline().rstrip().split())

arr = [[0 for _ in range(K+1)] for _ in range(N+1)]
thing = [[0, 0]]

for i in range(N):
    thing.append(list(map(int, stdin.readline().rstrip().split())))

for j in range(1, N+1):
    for k in range(1, K+1):
        w = thing[j][0]
        v = thing[j][1]
        
        if w > k:
            arr[j][k] = arr[j-1][k]
        else:
            arr[j][k] = max(arr[j-1][k], arr[j-1][k-w] + v)
print(arr[N][K])
