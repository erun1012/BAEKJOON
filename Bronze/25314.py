from sys import stdin

N = int(stdin.readline().rstrip())

for i in range(N // 4):
    print("long", end=" ")
print("int")