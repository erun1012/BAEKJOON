from sys import stdin

n = int(stdin.readline())

arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    get_arr = list(map(int, stdin.readline().rstrip().split()))
    for j in range(0, len(get_arr)):
        arr[i][j] = get_arr[j]

for k in range(1, n):
    for l in range(n):
        if l == 0:
            arr[k][l] += arr[k-1][l]
        else:
            arr[k][l] += max(arr[k-1][l-1], arr[k-1][l])
print(max(arr[-1]))
