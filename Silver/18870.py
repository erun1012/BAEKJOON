from sys import stdin

N = int(stdin.readline())
arr = list(map(lambda x: [int(x), 0, 0], stdin.readline().rstrip().split()))
num = 0
for i in arr:
    i[2] = num
    num += 1

arr.sort(key=lambda x: x[0])
cnt = 0
for i in range(1, N):
    if arr[i][0] != arr[i-1][0]:
        cnt += 1
    arr[i][1] = cnt
arr.sort(key=lambda x: x[2])
for i in arr:
    print(i[1], end=" ")
