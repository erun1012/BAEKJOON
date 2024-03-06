#참조: https://headf1rst.github.io/algorithm/totalSum/
from sys import stdin

def make_sum_arr(arr, N):
    sum_arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            sum_arr[i][j] = arr[i-1][j-1] + sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1]
    return sum_arr

N, M = map(int, stdin.readline().rstrip().split())

arr = [[0] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, stdin.readline().rstrip().split()))

sum_arr = make_sum_arr(arr, N)

for j in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().rstrip().split())
    print(sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1])
