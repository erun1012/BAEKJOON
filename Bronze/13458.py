from sys import stdin
input = stdin.readline

N = int(input())
A_list = list(map(int, input().rstrip().split()))
B, C = map(int, input().rstrip().split())

count = N
for i in A_list:
    if i - B <= 0:
        continue
    elif (i-B) % C != 0:
        count += ((i-B)//C + 1)
    else:
        count += (i-B)//C
print(count)
