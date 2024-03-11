from sys import stdin

N = int(stdin.readline())
get = list(map(int, stdin.readline().rstrip().split()))

arr = [1]*N

for i in range(0, N):
    for j in range(0, i):
        if get[i] > get[j]:
            arr[i] = max(arr[i], arr[j]+1)

if arr.index(max(arr))+1 == N:
    print(max(arr))
else:
    check = arr[arr.index(max(arr))+1:]
    check.reverse()
    check_arr = [1]*len(check)
    
    for k in range(0, len(check)):
        for l in range(0, k):
            if check[k] > check[l]:
                check_arr[k] = max(check_arr[k], check_arr[l]+1)
    print(max(arr)+max(check_arr))
