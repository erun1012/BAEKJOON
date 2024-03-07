from sys import stdin

total = int(stdin.readline())
for _ in range(9):
    total -= int(stdin.readline())
print(total)
