from sys import stdin

N = int(stdin.readline())
get = list(map(int, stdin.readline().rstrip().split()))
reverse_get = get[::-1]

increase_arr = [1 for _ in range(N)]
decrease_arr = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if get[i] > get[j]:
            increase_arr[i] = max(increase_arr[i], increase_arr[j]+1)
        if reverse_get[i] > reverse_get[j]:
            decrease_arr[i] = max(decrease_arr[i], decrease_arr[j]+1)


result = [0 for _ in range(N)]
decrease_arr.reverse()

for i in range(N):
    result[i] = increase_arr[i] + decrease_arr[i]-1
print(max(result))
