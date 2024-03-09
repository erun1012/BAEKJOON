from sys import stdin

N = int(stdin.readline())

for _ in range(N):
    trash = stdin.readline()
    print(sum(map(int, stdin.readline().rstrip().split())))
