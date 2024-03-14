from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    Class, Grade = 0, 0
    for i in range(N):
        C, G = map(str, stdin.readline().rstrip().split())
        Class += int(C)
        Grade += int(C)*float(G)
    print(Class, round(Grade/Class, 1))
