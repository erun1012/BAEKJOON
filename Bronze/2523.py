from sys import stdin

N = int(stdin.readline())

for i in range(1, N+1):
    print("*"*(i) + " "*(N-i))
for j in range(1, N):
    print("*"*(N-j) + " "*(j))
