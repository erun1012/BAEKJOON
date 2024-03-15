from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    s = int(stdin.readline())
    n = int(stdin.readline())
    for i in range(n):
        p, q = map(int, stdin.readline().rstrip().split())
        s += p*q
    print(s)
