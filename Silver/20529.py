from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    arr = list(map(str, stdin.readline().rstrip().split()))
    if N > 32:
        print(0)
    else:
        sum = []
        for i in range(0, len(arr)-2):
            for j in range(i+1, len(arr)-1):
                for k in range(j+1, len(arr)):
                    count = 0
                    for l in range(4):
                        if arr[i][l] != arr[j][l]:
                            count += 1
                        if arr[i][l] != arr[k][l]:
                            count += 1
                        if arr[j][l] != arr[k][l]:
                            count += 1
                    sum.append(count)
        print(min(sum))
