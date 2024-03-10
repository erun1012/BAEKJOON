from sys import stdin

N = int(stdin.readline())

arr = []

for i in range(N):
    A, B, C = map(int, stdin.readline().rstrip().split())
    arr.append([[A, A], [B, B], [C, C]])
    
    if len(arr) == 2:
        arr[1][0][0] += max(arr[0][0][0], arr[0][1][0])
        arr[1][1][0] += max(arr[0][0][0], arr[0][1][0], arr[0][2][0])
        arr[1][2][0] += max(arr[0][1][0], arr[0][2][0])
        arr[1][0][1] += min(arr[0][0][1], arr[0][1][1])
        arr[1][1][1] += min(arr[0][0][1], arr[0][1][1], arr[0][2][1])
        arr[1][2][1] += min(arr[0][1][1], arr[0][2][1])
        
        arr.pop(0)

print(max(arr[0][0][0], arr[0][1][0], arr[0][2][0]), min(arr[0][0][1], arr[0][1][1], arr[0][2][1]))
